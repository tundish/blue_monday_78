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

import collections
import datetime
import itertools
import os.path
import pathlib
import time
import sys

import pkg_resources

from turberfield.dialogue.model import SceneScript

from bluemonday78 import __version__ as version # noqa
from bluemonday78.matcher import MultiMatcher
from bluemonday78.types import Character
from bluemonday78.types import Location
from bluemonday78.types import Narrator
from bluemonday78.types import Character
from bluemonday78.types import Look
from bluemonday78.types import Mode
from bluemonday78.types import Trade
from bluemonday78.types import Spot
import bluemonday78.utils.publisher

blue_monday = datetime.date(1978, 1, 16)


def ensemble(narrator=None):
    rv = [
        Character(
            name="Mr Ray Farington"
        ).set_state(Look.veteran, Mode.guardian, Spot.w12_ducane_prison_wing),
        Character(
            name="Mr William Billy McCarthy"
        ).set_state(Look.youth, Mode.thief, Spot.w12_ducane_prison_wing),
        Character(
            name="Mrs Karen Sheppey"
        ).set_state(Look.punter, Mode.healer, Spot.w12_ducane_prison_visiting, 1),
        Character(
            name="Mr Martin Sheppey"
        ).set_state(Look.mug, Spot.w12_ducane_prison_wing),
        Character(
            name="Mr Barry Latimer"
        ).set_state(Trade.innkeeper, Spot.w12_goldhawk_tavern, 1),
        Character(name="Mr Ian Thomas").set_state(Spot.w12_goldhawk_tavern, 1),
        Character(name="Mr Mike Phillips").set_state(Spot.w12_goldhawk_tavern, 1),
        Character(
            name="Mr Justin Cornelis Delcroix"
        ).set_state(Look.yuppie, Trade.merchant, Spot.w12_goldhawk_tavern, 1),
        Character(name="Mr Matthew Waladli").set_state(Trade.singer),
        Location(label="Addison Arches 18A").set_state(Spot.w12_latimer_arches),
        Location(label="Visiting Suite").set_state(Spot.w12_ducane_prison_visiting),
        Location(label="Reception area").set_state(Spot.w12_ducane_prison_release),
        Location(label="Prison wing").set_state(Spot.w12_ducane_prison_wing),
        Location(label="The Goldhawk Tavern").set_state(Spot.w12_goldhawk_tavern),
    ]
    if narrator is not None:
        rv.append(narrator)
    return rv


def build_narrator(**kwargs):
    memories = kwargs.pop("memories", [])
    rv = Narrator(
        memories=collections.deque(memories, maxlen=max(6, len(memories))),
        **kwargs
    )
    if not kwargs:
        return rv.set_state(
            Spot.w12_ducane_prison_wing
        ).set_state(
            int(blue_monday.strftime("%Y%m%d0800"))
        )
    else:
        return rv


def generate_folders(pkg, path):
    root_path = pathlib.Path(pkg_resources.resource_filename(pkg, path))
    yield from (
        SceneScript.Folder(
            pkg="bluemonday78",
            description="Story arc: '{0}'".format(asset.arc.capitalize()),
            metadata={
                "id": asset.id,
                "arc": asset.arc,
                "pathways": asset.pathways
            },
            paths=[os.path.join(root_path.name, i) for i in asset.scripts],
            interludes=None
        )
        for asset in
        bluemonday78.utils.publisher.find_assets(
            root_path, prefix="{0}.{1}".format(pkg, path.replace("/", "."))
        )
    )


def prepare_folders(pkg="bluemonday78", path="dialogue", min_t=None, max_t=None):
    return [
        MultiMatcher.decorate_folder(f, min_t, max_t)
        for f in generate_folders(pkg, path)
    ]


def search(seq, typ=None, **kwargs):
    """ Search the sequence for objects matching criteria.

    If typ is specified, only instances of that type are
    matched. Any keyword arguments match an object by
    attribute.

    """
    return (
        i for i in seq
        if isinstance(i, typ or object)
        and (not kwargs or any(
            getattr(i, k, None) == v
            for k, v in kwargs.items()
        ))
    )


if __name__ == "__main__":
    then = time.perf_counter()
    results = prepare_folders()
    print(*results, sep="\n", file=sys.stdout)
    now = time.perf_counter()
    print("Processed {0} folders in {1:.3f}s.".format(len(results), now - then), file=sys.stderr)
