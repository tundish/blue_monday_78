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
import functools
import random
import sys
import uuid

from aiohttp import web
import pkg_resources

from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer

from bluemonday78.matcher import MultiMatcher
from bluemonday78.presenter import Presenter
import bluemonday78.render
import bluemonday78.story
from bluemonday78.types import Location
from bluemonday78.types import Spot


async def get_frame(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app.sessions[uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))

    folders = request.app.folders
    if not presenter.pending:
        dialogue = Presenter.dialogue(folders, presenter.ensemble)
        request.app.sessions[uid] = Presenter(dialogue, presenter.ensemble)

    try:
        frame = presenter.frame()
    except IndexError:
        print("Presenter has no more frames", file=sys.stderr)
        raise web.HTTPFound("/{0.hex}/map".format(uid))

    pending = presenter.pending
    return web.Response(
        text = bluemonday78.render.body_html(
            refresh=Presenter.refresh_animations(frame) if pending else None,
        ).format(bluemonday78.render.frame_to_html(
            frame, presenter.ensemble, not pending
        )),
        content_type="text/html"
    )


async def get_map(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app.sessions[uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))
    return web.Response(
        text = bluemonday78.render.body_html(
            refresh=None
        ).format(bluemonday78.render.ensemble_to_html(presenter.ensemble)),
        content_type="text/html"
    )


async def get_titles(request):
    return web.Response(
        text = bluemonday78.render.body_html(refresh=None).format(
            bluemonday78.render.titles_to_html()
        ),
        content_type="text/html"
    )


async def post_titles(request):
    data = await request.post()
    name = data["playername"]
    if not Presenter.validation["name"].match(name):
        raise web.HTTPUnauthorized(reason="User input invalid name.")

    player = bluemonday78.story.build_player(name)
    ensemble = bluemonday78.story.ensemble(player)
    dialogue = Presenter.dialogue(request.app.folders, ensemble)
    presenter = Presenter(dialogue, ensemble)
    print(player, file=sys.stderr)
    request.app.sessions[player.id] = presenter
    raise web.HTTPFound("/{0.id.hex}".format(player))


async def post_hop(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    try:
        presenter = request.app.sessions[uid]
    except KeyError:
        raise web.HTTPUnauthorized(reason="Session {0!s} not found.".format(uid))
    data = await request.post()
    location_id = uuid.UUID(hex=data["location_id"])
    location = next(i for i in presenter.ensemble if getattr(i, "id", None) == location_id)
    pathway = location.get_state(Spot).value
    matcher = MultiMatcher(request.app.folders)
    folders = list(matcher.options({"pathways": set([pathway])}))
    dialogue = Presenter.dialogue(folders, presenter.ensemble)
    if dialogue is not None:
        request.app.sessions[uid] = Presenter(dialogue, presenter.ensemble)
    raise web.HTTPFound("/{0.hex}".format(uid))


def build_app(args):
    app = web.Application()
    app.add_routes([
        web.get("/", get_titles),
        web.post("/", post_titles),
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
    ])
    app.router.add_static(
        "/css/",
        pkg_resources.resource_filename("bluemonday78", "static/css")
    )
    app.sessions = {}
    app.folders = bluemonday78.story.prepare_folders()
    return app


def main(args):
    app = build_app(args)
    return web.run_app(app, host=args.host, port=args.port)


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
