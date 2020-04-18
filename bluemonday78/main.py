#!/usr/bin/env python3
# encoding: UTF-8

# This file is part of Addison Arches.
#
# Addison Arches is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Addison Arches is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Addison Arches.  If not, see <http://www.gnu.org/licenses/>.


import argparse
import asyncio
from collections import deque
from collections import namedtuple
import configparser
import functools
import importlib.resources
import logging
import logging.config
import pathlib
import signal
import socket
import sys
import uuid

import aiohttp
from aiohttp import web
import pkg_resources

from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer
from turberfield.utils.assembly import Assembly

from bluemonday78.matcher import MultiMatcher
from bluemonday78.presenter import Presenter
import bluemonday78.render
import bluemonday78.story
from bluemonday78.types import Location
from bluemonday78.types import Narrator
from bluemonday78.types import Spot


async def get_frame(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))

    if not presenter.pending:
        presenter.log.debug("No frames pending. Finding new dialogue.")
        narrator = presenter.ensemble[-1]
        pathway = narrator.get_state(Spot).value
        matcher = MultiMatcher(request.app["folders"])
        folders = list(matcher.options({"pathways": set([pathway])}))
        dialogue = presenter.dialogue(folders, presenter.ensemble)
        request.app["sessions"][uid] = presenter = Presenter(dialogue, presenter.ensemble)

    try:
        frame = presenter.frame()
    except IndexError:
        raise web.HTTPFound("/{0.hex}/map".format(uid))

    pending = presenter.pending
    return web.Response(
        text = bluemonday78.render.body_html(
            refresh=Presenter.refresh_animations(frame) if pending else None,
        ).format(
            bluemonday78.render.dict_to_css(presenter.definitions),
            bluemonday78.render.frame_to_html(
                frame, presenter.ensemble, not pending
            )
        ),
        content_type="text/html"
    )


async def get_map(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))
    return web.Response(
        text = bluemonday78.render.body_html(
            refresh=None
        ).format(
            bluemonday78.render.dict_to_css(presenter.definitions),
            bluemonday78.render.ensemble_to_html(presenter.ensemble)
        ),
        content_type="text/html"
    )


async def get_titles(request):
    return web.Response(
        text = bluemonday78.render.body_html(refresh=None).format(
            bluemonday78.render.dict_to_css(Presenter.definitions),
            bluemonday78.render.titles_to_html(
                config=next(iter(request.app["config"]), None)
            )
        ),
        content_type="text/html"
    )


async def post_titles(request):
    config=next(iter(request.app["config"]), None)
    data = await request.post()
    assembly_url = data.get("assembly_url")
    ensemble = []
    if assembly_url and config and config.getboolean("assembly", "enable_load", fallback=False):
        if not Presenter.validation["url"].match(assembly_url):
            raise web.HTTPUnauthorized(reason="User requested invalid URL.")

        try:
            async with request.app["client"].get(
                assembly_url, trace_request_ctx={"log_name": "app.client"}
            ) as response:

                if response.status != 200:
                    raise web.HTTPUnauthorized(reason=response.reason)

                text = await(response.text())
                try:
                    assembly = Assembly.loads(text)
                    ensemble = assembly.get("ensemble")
                except Exception as e:
                    request.app["log"].error(e)
                    raise web.HTTPUnauthorized(reason="Invalid data.")

        except (
            aiohttp.ClientResponseError, aiohttp.ClientConnectionError, aiohttp.ClientPayloadError,
            asyncio.TimeoutError,
        ) as e:
            request.app["log"].error(e)

        try:
            clone = next(i for i in reversed(ensemble) if isinstance(i, Narrator))
            narrator = bluemonday78.story.build_narrator(
                id=None,
                memories=clone.memories,
                _states=clone._states
            )
            ensemble.remove(clone)
            ensemble.append(narrator)
        except:
            ensemble = None

    if not ensemble:
        narrator = bluemonday78.story.build_narrator()
        ensemble = bluemonday78.story.ensemble(narrator)
    else:
        request.app["log"].info("Load successful from assembly")

    presenter = Presenter(None, ensemble)
    presenter.log.debug(narrator)
    request.app["sessions"][narrator.id] = presenter
    request.app["log"].info("session: {0.id.hex}".format(narrator))
    raise web.HTTPFound("/{0.id.hex}".format(narrator))


async def post_hop(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))

    data = await request.post()
    location_id = uuid.UUID(hex=data["location_id"])
    location = next(bluemonday78.story.search(presenter.ensemble, id=location_id))
    spot = location.get_state(Spot)

    narrator = presenter.ensemble[-1]
    narrator.set_state(spot)
    presenter.log.debug("Hopped to {0}".format(spot))

    pathway = spot.value
    matcher = MultiMatcher(request.app["folders"])
    folders = list(matcher.options({"pathways": set([pathway])}))
    dialogue = presenter.dialogue(folders, presenter.ensemble)
    if dialogue is None:
        request.app["log"].info("No new dialogue cast. Check selection.")
    else:
        request.app["sessions"][uid] = Presenter(dialogue, presenter.ensemble)
    raise web.HTTPFound("/{0.hex}".format(uid))


async def get_assembly(request):
    config=next(iter(request.app["config"]), None)
    if not (config and config.getboolean("assembly", "enable_dump", fallback=False)):
        raise web.HTTPUnauthorized(reason="Operation not enabled.")

    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))
    else:
        return web.Response(
            text=Assembly.dumps(presenter.assembly),
            content_type="application/json"
        )


async def get_metricz(request):
    data = {
        "host": {"name": socket.gethostname()},
        "sessions": [
            {
                "uid": str(uid),
            }
            for uid, presenter in request.app["sessions"].items()
        ]
    }
    return web.json_response(data)


class Config:

    @classmethod
    def build_app(cls):
        app = web.Application()
        app.add_routes([
            web.get("/", get_titles),
            web.post("/", post_titles),
            web.get("/metricz", get_metricz),
            web.get(
                "/{{session:{0}}}".format(
                    Presenter.validation["session"].pattern
                ),
                get_frame
            ),
            web.get(
                "/{{session:{0}}}/map".format(
                    Presenter.validation["session"].pattern
                ),
                get_map
            ),
            web.post(
                "/{{session:{0}}}/hop".format(
                    Presenter.validation["session"].pattern,
                ),
                post_hop
            ),
            web.get(
                "/{{session:{0}}}/assembly".format(
                    Presenter.validation["session"].pattern
                ),
                get_assembly
            ),
        ])

        app.router.add_static(
            "/css/",
            pkg_resources.resource_filename("bluemonday78", "static/css")
        )
        app.router.add_static(
            "/img/",
            pkg_resources.resource_filename("bluemonday78", "static/img")
        )
        app.router.add_static(
            "/fonts/",
            pkg_resources.resource_filename("bluemonday78", "static/fonts")
        )

        app["log"] = logging.getLogger("app")

        app["sessions"] = {}
        app["folders"] = bluemonday78.story.prepare_folders()

        return app

    @classmethod
    def parser(cls):
        cfg = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        cfg.optionxform = str
        return cfg

    @classmethod
    def read_config(cls, path=None):
        log = logging.getLogger("")
        if path and path.is_file():
            text = path.read_text()
            src = path.resolve()
        else:
            text = importlib.resources.read_text("bluemonday78", "default.cfg")
            src = "default.cfg"

        cfg = cls.parser()
        try:
            cfg.read_string(text, source=src)
        except Exception as e:
            log.exception(e)
            log.warning("Bad config")
        finally:
            return src, cfg

    @classmethod
    def load_config(cls, app, path, default_cfg):
        log = logging.getLogger("")
        log.info("Trying to load '{0}' ...".format(path))
        src, cfg = cls.read_config(path)
        log.info("Processed '{0}'".format(src))
        missing_sections = set(default_cfg.sections()).difference(set(cfg.sections()))
        if missing_sections:
            for section_name in missing_sections:
                log.warning("Missing section '{0}'".format(section_name))
            return src, None
        else:
            try:
                logging.config.fileConfig(cfg, disable_existing_loggers=False)
            except Exception as e:
                log.exception(e)

            try:
                app["config"].append(cfg)
            except (AttributeError, KeyError) as e:
                app["config"] = deque([cfg], maxlen=1)
                log.debug("First config is stored.")
            finally:
                return src, cfg

    @classmethod
    async def on_request_start(cls, session, trace_config_ctx, params):
        log = logging.getLogger(
            getattr(trace_config_ctx, "trace_request_ctx", {}).get("log_name", "")
        )
        log.info("{0.method} {0.url}".format(params))
        trace_config_ctx.start = asyncio.get_event_loop().time()

    @classmethod
    async def on_request_redirect(cls, session, trace_config_ctx, params):
        log = logging.getLogger(
            getattr(trace_config_ctx, "trace_request_ctx", {}).get("log_name", "")
        )
        log.warning("redirectd: {0}".format(params))

    @classmethod
    async def on_request_end(cls, session, trace_config_ctx, params):
        elapsed = asyncio.get_event_loop().time() - trace_config_ctx.start
        log = logging.getLogger(
            getattr(trace_config_ctx, "trace_request_ctx", {}).get("log_name", "")
        )
        log.info("status: {0.response.status}".format(params))
        log.info("elapsed time: {0}".format(elapsed))

    @classmethod
    async def on_shutdown(cls, app):
        await app["client"].close()

    @classmethod
    async def register_app_handlers(cls, app, host:str, port:int, loop=None):
        trace_config = aiohttp.TraceConfig()
        trace_config.on_request_start.append(cls.on_request_start)
        trace_config.on_request_redirect.append(cls.on_request_redirect)
        trace_config.on_request_end.append(cls.on_request_end)

        app["client"] = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(connect=6.0, total=8.0),
            trace_configs=[trace_config],
            trust_env=True
        )
        app.on_shutdown.append(cls.on_shutdown)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)

        return runner, site


def main(args, loop=None):
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s|%(name)s|%(message)s",
        level=logging.INFO
    )

    app = Config.build_app()

    src, default_cfg = Config.read_config()
    src, cfg = Config.load_config(app, args.config, default_cfg)
    if not cfg:
        logging.error("Bad config file '{0}'".format(src))
        return 1
    else:
        logging.info("Accepted config file '{0}'".format(src))

    loop = loop or asyncio.get_event_loop()
    try:
        loop.add_signal_handler(signal.SIGINT, functools.partial(loop.call_soon, loop.stop))
        loop.add_signal_handler(signal.SIGTERM, functools.partial(loop.call_soon, loop.stop))
        loop.add_signal_handler(
            signal.SIGHUP, functools.partial(
                loop.call_soon, Config.load_config, app, args.config, default_cfg
            )
        )
    except NotImplementedError:
        logging.warning("No signal handlers are available")
    finally:
        asyncio.set_event_loop(loop)

    runner, site = loop.run_until_complete(Config.register_app_handlers(app, args.host, args.port))
    try:
        logging.info("Serving from {0.host} on port {0.port}".format(args))
        loop.run_until_complete(site.start())
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Caught keyboard interrupt.")
        pass
    except Exception as e:
        logging.exception(e)
    finally:
        logging.info("Tidying up...")
        loop.run_until_complete(runner.cleanup())
        loop.close()
        logging.info("Complete.")


def parser(description=__doc__):
    rv = argparse.ArgumentParser(description)
    rv.add_argument(
        "--version", action="store_true", default=False,
        help="Print the current version number.")
    rv.add_argument(
        "--host", default="127.0.0.1",
        help="Set an interface on which to serve."
    )
    rv.add_argument(
        "--port", default=8080, type=int,
        help="Set a port on which to serve."
    )
    rv.add_argument(
        "--config", default=None, type=pathlib.Path,
        help="Specify a config file."
    )
    return rv


def run():
    p = parser()
    args = p.parse_args()

    rv = 0
    if args.version:
        sys.stdout.write(bluemonday78.__version__)
        sys.stdout.write("\n")
    else:
        rv = main(args)

    if rv == 2:
        sys.stderr.write("\n Missing command.\n\n")
        p.print_help()

    sys.exit(rv)


if __name__ == "__main__":
    run()
