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

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import Player

from bluemonday78 import __version__ as version # noqa
from bluemonday78.associations import Associations
from bluemonday78.paths import GoldenPath
from bluemonday78.types import Barman
from bluemonday78.types import Character
from bluemonday78.types import Hipster
from bluemonday78.types import Location
from bluemonday78.types import Narrator
from bluemonday78.types import NoteBook
from bluemonday78.types import Prisoner
from bluemonday78.types import PrisonOfficer
from bluemonday78.types import PrisonVisitor
from bluemonday78.types import Spot
from bluemonday78.types import Travel
from bluemonday78.types import Via
from bluemonday78.types import Visibility

blue_monday = datetime.date(1978, 1, 16)

def associations():
    rv = Associations()
    rv.register(
        None, *(
            i.set_state(int(blue_monday.strftime("%Y%m%d0800")))
            for i in (
                Narrator().set_state(Spot.w12_ducane_prison_visiting),
                Player(name="Mr Likely Story").set_state(Spot.w12_ducane_prison_wing),
                Barman(name="Mr Barry Latimer").set_state(Spot.w12_goldhawk_tavern),
                Hipster(name="Mr Justin Cornelis Delcroix").set_state(Spot.w12_goldhawk_tavern),
                PrisonOfficer(name="Mr Ray Farington").set_state(Spot.w12_ducane_prison_wing),
                Prisoner(name="Mr Martin Sheppey").set_state(Spot.w12_ducane_prison_wing),
                PrisonVisitor(name="Mrs Karen Sheppey").set_state(Spot.w12_ducane_prison),
                Character(name="Mr Ian Thomas").set_state(Spot.w12_goldhawk_tavern),
                Character(name="Mr Mike Phillips").set_state(Spot.w12_goldhawk_tavern),
                Character(name="Mr Matthew Waladli").set_state(Spot.w12_goldhawk_tavern),
            )
        ),
        NoteBook().set_state(Visibility.hidden),
        Location(label="Addison Arches 18A").set_state(Spot.w12_latimer_arches),
        Location(label="Wormwood Scrubs").set_state(Spot.w12_ducane_prison),
        Location(label="Wormwood Scrubs visiting").set_state(Spot.w12_ducane_prison_visiting),
        Location(label="Wormwood Scrubs reception").set_state(Spot.w12_ducane_prison_release),
        Location(label="Wormwood Scrubs prison wing").set_state(Spot.w12_ducane_prison_wing),
    )
    return rv


references = list(associations().ensemble()) + [Spot, Travel, Via, Visibility]


local = SceneScript.Folder(
    pkg="bluemonday78",
    description="Location-specific elaboration.",
    metadata={"timestamp": blue_monday},
    paths=[
        "w12_19780116_local/w12_latimer_arches_19780116.rst",
        "w12_19780116_local/w12_latimer_arches_19780117.rst",
    ],
    interludes=itertools.repeat(None)
)


justin = SceneScript.Folder(
    pkg="bluemonday78",
    description="Justin Delcroix has just got the sack.",
    metadata={"timestamp": blue_monday},
    paths=[
        "justin_19780116_fired/sorrows.rst",
        "justin_19780116_fired/anguish.rst",
        "justin_19780116_fired/desparation.rst"
    ],
    interludes=itertools.repeat(None)
)

ray = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata={"timestamp": blue_monday},
    paths=[
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/escape.rst",
        "ray_19780116_retires/homecoming.rst",
    ],
    interludes=itertools.repeat(None)
)

ray = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata={"timestamp": blue_monday},
    paths=[
        "ray_19780116_retires/step_forward.rst",
        "ray_19780116_retires/getting_here.rst",
        "ray_19780116_retires/hows_work.rst",
        "ray_19780116_retires/these_keys.rst",
        "ray_19780116_retires/pocket_fax.rst",
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/frankly.rst",
        "ray_19780116_retires/transfer.rst",
        "ray_19780116_retires/escape.rst",
    ],
    interludes=[
        GoldenPath.locate_to_karen,
        GoldenPath.locate_to_karen,
        GoldenPath.locate_to_karen,
        GoldenPath.locate_to_ray,
        GoldenPath.locate_to_ray,
        GoldenPath.locate_to_ray,
        GoldenPath.locate_to_karen,
        GoldenPath.locate_to_ray,
        GoldenPath.stop,
    ]
)

plotlines = (justin, ray)
schedule = collections.deque([local])
schedule.extendleft(plotlines)
