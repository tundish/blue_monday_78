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

from aiohttp import web
import pkg_resources

from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer

from bluemonday78.presenter import Presenter
import bluemonday78.render
import bluemonday78.story
from bluemonday78.types import Location


class Presentation:

    Element = namedtuple(
        "Element",
        ["source", "dialogue", "shot", "offset", "duration"]
    )

    @staticmethod
    def build_frames(source, seq, dwell, pause):
        """Generate a new Frame on each Shot and FX item"""
        shot = None
        frame = []
        offset = 0
        for item in seq:
            if isinstance(item, (Model.Audio, Model.Shot)):
                if frame and shot and shot != item:
                    yield frame
                    frame = []
                    offset = 0

                if isinstance(item, Model.Shot):
                    shot = item
                else:
                    frame.append(Presentation.Element(
                        source, item, shot,
                        item.offset / 1000,
                        item.duration / 1000
                    ))

            elif isinstance(item, Model.Line):
                durn = pause + dwell * item.text.count(" ")
                frame.append(Presentation.Element(
                    source, item, shot, offset, durn
                ))
                offset += durn
            elif not isinstance(item, Model.Condition):
                frame.append(Presentation.Element(
                    source, item, shot, offset, 0
                ))
        else:
            if any(
                isinstance(
                    i.dialogue, (Model.Audio, Model.Line)
                )
                for i in frame
            ):
                yield frame

    @staticmethod
    def next_frame(session, entities, dwell=0.3, pause=1):
        while not session["frames"]:
            location = session["state"].area
            matcher = Matcher(bluemonday78.sbluemonday78y.episodes)
            folders = list(matcher.options(session["metadata"]))
            performer = Performer(folders, entities)
            folder, index, script, selection, interlude = performer.next(
                folders, entities
            )
            scene = performer.run(react=False)
            frames = list(Presentation.build_frames(
                folder.paths[index], scene,
                dwell=dwell, pause=pause
            ))
            session["frames"].extend(frames)

        return session["frames"].popleft()

    @staticmethod
    def react(session, frame):
        for element in frame:
            event = element.dialogue
            if (
                isinstance(event, Model.Property) and
                event.object is not None
            ):
                setattr(event.object, event.attr, event.val)

            yield element

    @staticmethod
    def refresh(frame, min_val=8):
        try:
            return max(
                [min_val] +
                [i.offset + i.duration for i in frame if i.duration]
            )
        except ValueError:
            return None


async def get_frame(request):
    session = request.app.session
    #location = session["state"].area
    player = bluemonday78.logic.Player(
        name="Mr William Billy McCarthy",
    ).set_state(bluemonday78.logic.Spot.w12_ducane_prison)
    entities = [
        i for i in bluemonday78.story.ensemble
        if getattr(i, "area", location) == location
    ]
    narrator = next(i for i in entities if isinstance(i, Narrator))
    narrator.state = session["state"]
    for character in (i for i in entities if isinstance(i, Character)):
        character.set_state(random.randrange(10))

    frame = Presentation.next_frame(session, entities)
    buys = ["Spend 1c", "Spend 2c", "Spend 3c"] if location == "butcher" else []
    cuts = ["Cut less", "Cut same", "Cut more"] if location == "chamber" else []
    hops = bluemonday78.rules.topology[location]
    elements = list(Presentation.react(session, frame))
    return web.Response(
        text = bluemonday78.render.base_to_html(
            #refresh=math.ceil(Presentation.refresh(frame))
            refresh=None
        ).format(
            bluemonday78.render.body_to_html(session["state"], frame=frame).format(
                "\n".join(
                    bluemonday78.render.element_as_list_item(element)
                    for element in frame
                ),
                "\n".join(
                    bluemonday78.render.option_as_list_item(n, option, path="/hop/")
                    for n, option in enumerate(hops)
                ),
                "\n".join(
                    bluemonday78.render.option_as_list_item(n + 1, option, path="/buy/")
                    for n, option in enumerate(buys)
                ),
                "\n".join(
                    bluemonday78.render.option_as_list_item(n, option, path="/cut/")
                    for n, option in enumerate(cuts)
                ),
            )
        ),
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
        web.get("/", get_frame),
        web.get("/map", get_map),
        #web.post("/buy/{{buy:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_buy),
        #web.post("/cut/{{cut:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_cut),
        #web.post("/hop/{{hop:{0}}}".format(bluemonday78.rules.choice_validabluemonday78.pattern), post_hop),
    ])
    app.router.add_static(
        "/css/",
        pkg_resources.resource_filename("bluemonday78", "static/css")
    )
    app.session = {
        "metadata": {"area": "balcony"},
        "frames": deque([])
    }
    return app


def main(args):
    app = build_app(args)
    app.ensemble = list(bluemonday78.story.associations().ensemble())
    # TODO: Move to game screen. Create player.
    dialogue = Presenter.dialogue(
        bluemonday78.story.folders,
        app.ensemble
    )
    app.presenter = Presenter(dialogue)
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
