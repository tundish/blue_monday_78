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
import math
import random
import sys
import uuid

from aiohttp import web
import pkg_resources

from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer

from bluemonday78.matcher import PathwayMatcher
from bluemonday78.presenter import Presenter
import bluemonday78.render
import bluemonday78.story
from bluemonday78.types import Location


async def get_demo(request):
    player = next(iter(request.app.sessions.values())).ensemble[-1]
    raise web.HTTPFound("/{0.id.hex}".format(player))

async def get_frame(request):
    uid = uuid.UUID(hex=request.match_info["session"])
    presenter = request.app.sessions[uid]
    folders = request.app.folders
    if not presenter.pending:
        dialogue = Presenter.dialogue(folders, presenter.ensemble)
        request.app.sessions[uid] = Presenter(dialogue, presenter.ensemble)
    frame = presenter.frame()
    return web.Response(
        text = bluemonday78.render.body_html(
            #refresh=math.ceil(Presentation.refresh(frame))
            refresh=None
        ).format(bluemonday78.render.frame_to_html(frame)),
        content_type="text/html"
    )


async def get_map(request):
    presenter = request.app.presenter
    ensemble = request.app.ensemble
    frame = presenter.frame()
    return web.Response(
        text = bluemonday78.render.body_html(
            #refresh=math.ceil(Presentation.refresh(frame))
            refresh=None
        #).format(bluemonday78.render.frame_to_html(frame)),
        ).format(bluemonday78.render.ensemble_to_html([i for i in ensemble if isinstance(i, Location)])),
        content_type="text/html"
    )

async def post_buy(request):
    buy = request.match_info["buy"]
    if not bluemonday78.rules.choice_validabluemonday78.match(buy):
        raise web.HTTPUnauthorized(reason="User sent invalid buy code.")
    else:
        session = request.app.session
        session["frames"].clear()
        rv = bluemonday78.rules.apply_rules(
            None, None, None, bluemonday78.rules.Settings, session["state"], buy=int(buy)
        )
        session["state"] = bluemonday78.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_cut(request):
    cut = request.match_info["cut"]
    if not bluemonday78.rules.choice_validabluemonday78.match(cut):
        raise web.HTTPUnauthorized(reason="User sent invalid cut code.")
    else:
        session = request.app.session
        session["frames"].clear()
        cut_d = {
            0: -bluemonday78.rules.Settings.CUT_D,
            1: 0,
            2: bluemonday78.rules.Settings.CUT_D,
        }.get(int(cut), bluemonday78.rules.Settings.CUT_D)

        rv = bluemonday78.rules.apply_rules(
            None, None, None, bluemonday78.rules.Settings, session["state"], cut=cut_d
        )
        session["state"] = bluemonday78.rules.State(**rv)
        raise web.HTTPFound("/")


async def post_hop(request):
    hop = request.match_info["hop"]
    if not bluemonday78.rules.choice_validabluemonday78.match(hop):
        raise web.HTTPUnauthorized(reason="User sent invalid hop.")
    else:
        index = int(hop)
        session = request.app.session
        location = session["state"].area
        destination = bluemonday78.rules.topology[location][index]
        session["metadata"]["area"] = destination
        session["state"] = session["state"]._replace(area=destination)
        session["frames"].clear()
        if destination not in ("butcher", "chamber"):
            rv = bluemonday78.rules.apply_rules(
                None, None, None, bluemonday78.rules.Settings, session["state"]
            )
            if not rv:
                print("Game Over", file=sys.stderr)
                rapunzel = next(
                    i for i in bluemonday78.sbluemonday78y.ensemble
                    if isinstance(i, Rapunzel)
                )
                rapunzel.set_state(At.club)
            else:
                session["state"] = bluemonday78.rules.State(**rv)
        raise web.HTTPFound("/")


def build_app(args):
    app = web.Application()
    app.add_routes([
        web.get("/demo", get_demo),
        web.get(
            "/{{session:{0}}}".format(
                Presenter.validation["session"].pattern
            ),
            get_frame
        ),
        web.get("/map", get_map),
        #web.post("/buy/{{buy:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_buy),
        #web.post("/cut/{{cut:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_cut),
        #web.post("/hop/{{hop:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_hop),
    ])
    app.router.add_static(
        "/css/",
        pkg_resources.resource_filename("bluemonday78", "static/css")
    )
    app.sessions = {}
    app.folders = bluemonday78.story.folders()
    return app


def main(args):
    app = build_app(args)
    # TODO: Move to game screen. Create player.
    player = bluemonday78.types.Player(
        name="Mr William Billy McCarthy",
    ).set_state(bluemonday78.types.Spot.w12_ducane_prison)
    ensemble = list(bluemonday78.story.associations().ensemble())
    ensemble.append(player)
    dialogue = Presenter.dialogue(app.folders, ensemble)
    app.sessions[player.id] = Presenter(dialogue, ensemble)
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
