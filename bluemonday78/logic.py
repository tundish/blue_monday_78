#!/usr/bin/env python
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
import enum
import itertools

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Player
from turberfield.dialogue.types import Stateful

from bluemonday78 import __version__ as version
from bluemonday78.test.paths import GoldenPath

class Attitude(EnumFactory, enum.Enum):
    neutral = 0
    grumpy = 1
    affable = 2

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d"
    w12_ducane_prison_visiting = "gcpv4d252v5y"
    w12_ducane_prison_release = "gcpv4d1qmdzb"
    w12_ducane_prison_wing = "gcpv4d1qrstu"  # TODO: recalculate
    w12_goldhawk_cafe = "gcpufzg2512x"
    w12_goldhawk_tavern = "gcpufzbd8x5d"
    w12_latimer_arches = "gcpv4cxb3dh4"

class Via(EnumFactory, enum.Enum):
    block = 0
    forwd = 1
    bckwd = 2
    bidir = 3

class Narrator(Stateful): pass
class PrisonOfficer(Stateful, Persona): pass
class Prisoner(Stateful, Persona): pass
class PrisonVisitor(Stateful, Persona): pass
class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass
class Character(Stateful, Persona): pass
class Location(Stateful, DataObject): pass


blue_monday = datetime.date(1978, 1, 16)


class Associations:

    def __init__(self):
        self.lookup = collections.OrderedDict([])

    def clear(self):
        for rels in self.lookup.values():
            for objs in rels.values():
                objs.clear()

    def ensemble(self, *args, **kwargs):
        return self.lookup.keys()

    def register(self, rel, primary, *args, **kwargs):
        subjects = set(args)
        for obj in {primary} | subjects:
            if obj not in self.lookup:
                self.lookup[obj] = collections.defaultdict(set)
        if rel is not None:
            self.lookup[primary][rel].update(subjects)
        return self

    def search(self, **kwargs):
        return set(
            i for i in self.lookup.keys()
            for k, v in kwargs.items()
            if getattr(i, k, None) == v
        )


def associations():
    rv = Associations()
    rv.register(
        None,
        *(i.set_state(int(blue_monday.strftime("%Y%m%d")))
          for i in (
            Narrator().set_state(Spot.w12_ducane_prison_visiting),
            Player(name="Mr Likely Story").set_state(Spot.w12_ducane_prison),
            Barman(
                name="Mr Barry Latimer"
            ).set_state(
                Attitude.neutral
            ).set_state(
                Spot.w12_goldhawk_tavern
            ),
            Hipster(name="Mr Justin Cornelis Delcroix").set_state(
                Spot.w12_goldhawk_tavern),
            PrisonOfficer(name="Mr Ray Farington").set_state(Spot.w12_ducane_prison_visiting),
            Prisoner(name="Mr Martin Sheppey").set_state(Spot.w12_ducane_prison),
            PrisonVisitor(name="Mrs Karen Sheppey").set_state(Spot.w12_ducane_prison),
            Character(name="Mr Ian Thomas").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Mike Phillips").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Matthew Waladli").set_state(Spot.w12_goldhawk_tavern),
          )
        ),
        Location(label="Addison Arches 18A").set_state(Spot.w12_latimer_arches),
        Location(label="Wormwood Scrubs").set_state(Spot.w12_ducane_prison),
        Location(label="Wormwood Scrubs visiting").set_state(Spot.w12_ducane_prison_visiting),
        Location(label="Wormwood Scrubs reception").set_state(Spot.w12_ducane_prison_release),
        Location(label="Wormwood Scrubs prison wing").set_state(Spot.w12_ducane_prison_wing),
    )
    return rv

references = list(associations().ensemble()) + [Attitude, Spot, Via]


local = SceneScript.Folder(
    pkg="bluemonday78",
    description="Location-specific elaboration.",
    metadata=[blue_monday],
    paths=[
        "w12_19780116_local/w12_latimer_arches_19780116.rst",
        "w12_19780116_local/w12_latimer_arches_19780117.rst",
    ],
    interludes=itertools.repeat(None)
)


justin = SceneScript.Folder(
    pkg="bluemonday78",
    description="Justin Delcroix has just got the sack.",
    metadata=[blue_monday],
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
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/escape.rst",
        "ray_19780116_retires/homecoming.rst",
    ],
    interludes=itertools.repeat(None)
)

fade_in = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/step_forward.rst",
    ],
    interludes=itertools.repeat(GoldenPath.listen_to_karen)
)
plotlines = (justin, ray)
schedule = collections.deque([local])
schedule.extendleft(plotlines)
