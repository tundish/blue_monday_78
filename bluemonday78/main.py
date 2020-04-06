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

"""
Hop to spots for debugging::

    python3 -m bluemonday78.main --spot w12_ducane_prison_wing --spot w12_ducane_prison_visiting

"""

import argparse
import asyncio
from collections import deque
from collections import namedtuple
import configparser
import functools
import importlib.resources
import logging
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
from bluemonday78.types import Spot


async def get_frame(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))

    if not presenter.pending:
        presenter.log.debug("No frames pending. Finding new dialogue.")
        player = presenter.ensemble[-1]
        pathway = player.get_state(Spot).value
        matcher = MultiMatcher(request.app["folders"])
        folders = list(matcher.options({"pathways": set([pathway])}))
        dialogue = Presenter.dialogue(folders, presenter.ensemble)
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
            bluemonday78.render.titles_to_html()
        ),
        content_type="text/html"
    )


async def post_titles(request):
    data = await request.post()
    assembly_url = data.get("assembly_url")
    ensemble = []
    if assembly_url:
        if not Presenter.validation["url"].match(assembly_url):
            raise web.HTTPUnauthorized(reason="User requested invalid URL.")

        request.app["log"].info(assembly_url)
        async with request.app["client"].get(assembly_url) as response:
            request.app["log"].info(response.status)

            if response.status != 200:
                raise web.HTTPUnauthorized(reason=response.reason)

            text = await(response.text())
            try:
                assembly = Assembly.loads(text)
                ensemble = assembly.get("ensemble")
            except Exception as e:
                request.app["log"].error(e)
                raise web.HTTPUnauthorized(reason="Invalid data.")

        try:
            clone = next(i for i in reversed(ensemble) if isinstance(i, bluemonday78.story.Player))
            player = bluemonday78.story.build_player(
                clone.name,
                id=None,
                memories=clone.memories,
                _states=clone._states
            )
            ensemble.remove(clone)
            ensemble.append(player)
        except:
            ensemble = None

    if not ensemble:
        player = bluemonday78.story.build_player(name=bluemonday78.story.player_name)
        ensemble = bluemonday78.story.ensemble(player)

    presenter = Presenter(None, ensemble)
    request.app["log"].info(player)
    request.app["sessions"][player.id] = presenter
    raise web.HTTPFound("/{0.id.hex}".format(player))


async def post_hop(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app["sessions"][uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))
    data = await request.post()
    location_id = uuid.UUID(hex=data["location_id"])
    location = next(bluemonday78.story.search(presenter.ensemble, id=location_id))
    pathway = location.get_state(Spot).value
    matcher = MultiMatcher(request.app["folders"])
    folders = list(matcher.options({"pathways": set([pathway])}))
    dialogue = Presenter.dialogue(folders, presenter.ensemble)
    if dialogue is None:
        request.app["log"].info("No new dialogue cast. Check selection.")
    else:
        request.app["sessions"][uid] = Presenter(dialogue, presenter.ensemble)
    raise web.HTTPFound("/{0.hex}".format(uid))


async def get_assembly(request):
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


async def on_shutdown(app):
    await app["client"].close()


class Config:

    @staticmethod
    def parser():
        cfg = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        cfg.optionxform = str
        return cfg

    @staticmethod
    def read_config(path):
        if path.is_file():
            text = path.read_text()
            src = path.resolve()
        else:
            text = importlib.resources.read_text("bluemonday78", "default.cfg")
            src = "default.cfg"

        cfg = Config.parser()
        cfg.read_string(text, source=src)
        return src, cfg

    @staticmethod
    def load_config(app, path):
        pass
        
    @staticmethod
    def build_app(cfg):
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

        # TODO: Optional config for dev only.
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
        #app["args"] = args
        app["log"] = logging.getLogger("app")

        app["sessions"] = {}
        app["folders"] = bluemonday78.story.prepare_folders()

        return app

    @staticmethod
    def load_config(app, path):
        pass

    @staticmethod
    async def register_app_handlers(app, args, loop=None):
        tracer = aiohttp.TraceConfig() # TODO: Add logging to callbacks

        # TODO: Add kill signal handlers

        app["client"] = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(connect=1.0, total=6.0),
            trace_configs=[tracer],
            trust_env=True
        )
        app.on_shutdown.append(on_shutdown)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, args.host, args.port)

        return runner, site


def main(args, loop=None):
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s|%(name)s|%(message)s",
        level=logging.INFO
    )

    src, cfg = Config.read_config(args.config)
    logging.info("Accepting config file {0}".format(src))

    app = Config.build_app(cfg)

    loop = loop or asyncio.get_event_loop()
    try:
        loop.add_signal_handler(signal.SIGINT, functools.partial(loop.call_soon, loop.stop))
        loop.add_signal_handler(signal.SIGTERM, functools.partial(loop.call_soon, loop.stop))
        loop.add_signal_handler(
            signal.SIGHUP, functools.partial(loop.call_soon, Config.load_config, app, args.config)
        )
    except NotImplementedError:
        # No signals available on Windows
        pass
    finally:
        asyncio.set_event_loop(loop)

    runner, site = loop.run_until_complete(Config.register_app_handlers(app, args))
    try:
        logging.info("Serving from {0._host} on port {0._port}".format(site))
        loop.run_until_complete(site.start())
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Caught keyboard interrupt.")
        pass
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
