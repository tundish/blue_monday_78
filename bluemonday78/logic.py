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
import logging
import re

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Player
from turberfield.dialogue.types import Stateful

class MatchMaker:

    lookup = collections.defaultdict(list)
    Phrase = collections.namedtuple("Phrase", ["gist", "variants"])

    @classmethod
    def register(cls, phrase):
        for v in phrase.variants:
            cls.lookup[cls.tokenize(v)].append(phrase)
        return phrase

    @staticmethod
    def tokenize(text):
        return tuple(re.sub("[^a-z ]+", "", text.lower()).split())

    @classmethod
    def match(cls, text):
        key = tuple(i for i in cls.tokenize(text) if i in cls.words())
        return iter(cls.lookup.get(key, []))

    @classmethod
    def words(cls):
        return set(i for k in cls.lookup for i in k)

class Attitude(EnumFactory, enum.Enum):
    neutral = 0
    grumpy = 1
    affable = 2

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d"
    w12_ducane_prison_visiting = "gcpv4d252v5y"
    w12_ducane_prison_release = "gcpv4d1qmdzb"
    w12_goldhawk_cafe = "gcpufzg2512x"
    w12_goldhawk_tavern = "gcpufzbd8x5d"
    w12_latimer_arches = "gcpv4cxb3dh4"

class Narrator(Stateful): pass
class PrisonOfficer(Stateful, Persona): pass
class Prisoner(Stateful, Persona): pass
class PrisonVisitor(Stateful, Persona): pass
class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass
class Character(Stateful, Persona): pass


blue_monday = datetime.date(1978, 1, 16)

def ensemble():
    return [
        i.set_state(int(blue_monday.strftime("%Y%m%d")))
        for i in (
            Narrator().set_state(Spot.w12_ducane_prison),
            Player(name="Mr Likely Story").set_state(Spot.w12_ducane_prison),
            Barman(name="Mr Barry Latimer").set_state(Spot.w12_goldhawk_tavern),
            Hipster(name="Mr Justin Cornelis Delcroix").set_state(
                Spot.w12_goldhawk_tavern),
            PrisonOfficer(name="Mr Ray Farington").set_state(Spot.w12_ducane_prison_visiting),
            Prisoner(name="Mr Martin Sheppey").set_state(Spot.w12_ducane_prison),
            PrisonVisitor(name="Mrs Karen Sheppey").set_state(Spot.w12_ducane_prison),
            Character(name="Mr Ian Thomas").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Mike Phillips").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Matthew Waladli").set_state(Spot.w12_goldhawk_tavern)
        )
    ]


references = ensemble() + [Attitude, Spot]

phrases = [
    MatchMaker.register(MatchMaker.Phrase(
        "Too right.",
        ["OK", "okay", "yes", "I agree"]
    )),
    MatchMaker.Phrase(
        "This is Frankie Marshall's place. Now go away.",
        ["frankie", "go away", "leave", "off"]
    ),
    MatchMaker.Phrase(
        "If you can't get rid of the family skeleton, "
        "you may as well make it dance.",
        ["family", "skeleton", "dance"]
    ),
]

def interlude(folder, index, ensemble, branches, phrase=None, log=None, loop=None):
    """
    This function manipulates the Narrator. The action follows.

    """
    log = log or logging.getLogger("bluemonday.logic")
    if not branches:
        return

    log.debug(branches)
    narrator = next(i for i in ensemble if isinstance(i, Narrator))
    if folder.paths == ray.paths:
        narrator.set_state(Spot.w12_goldhawk_tavern)
    elif folder.paths == justin.paths:
        narrator.set_state(Spot.w12_latimer_arches)
    else:
        narrator.set_state(Spot.w12_ducane_prison)

    try:
        match = phrases.index(phrase)
        log.debug(phrase)
    except ValueError:
        pass

    print(branches)
    branches.rotate(-1)
    print(branches)

    log.info("Narrator at {0}".format(narrator.get_state(Spot).name))
    return branches[0]

local = SceneScript.Folder(
    pkg="bluemonday78",
    description="Location-specific elaboration.",
    metadata=[blue_monday],
    paths=[
        "w12_19780116_local/w12_latimer_arches.rst",
        "w12_19780116_local/w12_goldhawk_tavern.rst",
    ],
    interludes=itertools.repeat(interlude)
)

justin = SceneScript.Folder(
    pkg="bluemonday78",
    description="Justin Delcroix has just got the sack.",
    metadata=[blue_monday],
    paths=[
        "justin_19780116_fired/sorrows.rst",
        "justin_19780116_fired/offence.rst",
        "justin_19780116_fired/anguish.rst",
        "justin_19780116_fired/offence.rst",
        "justin_19780116_fired/desparation.rst"
    ],
    interludes=itertools.repeat(interlude)
)

ray = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/homecoming.rst",
        "ray_19780116_retires/escape.rst",
    ],
    interludes=itertools.repeat(interlude)
)

plotlines = (justin, ray)
schedule = collections.deque([local])
schedule.extendleft(plotlines)
