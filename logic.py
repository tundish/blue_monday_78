#!/usr/bin/env python
#   -*- encoding: UTF-8 -*-

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
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Player
from turberfield.dialogue.types import Stateful

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d2dm6v2"
    w12_goldhawk_cafe = "gcpufzg2512x"
    w12_goldhawk_tavern = "gcpufzbd8x5d"
    w12_latimer_arches = "gcpv4cxb3dh4"

class PrisonOfficer(Stateful, Persona): pass
class Prisoner(Stateful, Persona): pass
class PrisonVisitor(Stateful, Persona): pass
class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass


blue_monday = datetime.date(1978, 1, 16)

ensemble = [
    Barman(name="Mr Barry Latimer").set_state(Spot.w12_goldhawk_tavern),
    Hipster(name="Mr Justin Cornelis Delcroix").set_state(Spot.w12_goldhawk_tavern),
    PrisonOfficer(name="Mr Ray Farington").set_state(Spot.w12_ducane_prison),
    Prisoner(name="Mr Martin Sheppey"),
    PrisonVisitor(name="Mrs Karen Sheppey"),
]

references = ensemble + [Spot]

schedule = collections.deque([])

def interlude(folder, index, ensemble, branches, cmd="", log=None, loop=None):
    branches.rotate(-1)
    return branches[0]

justin = SceneScript.Folder(
    pkg=__name__,
    description="Justin Delcroix has just got the sack.",
    metadata=[blue_monday],
    paths=["justin_19780116_fired/sorrows.rst"],
    interludes=itertools.repeat(interlude)
)

ray = SceneScript.Folder(
    pkg=__name__,
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/homecoming.rst",
        "ray_19780116_retires/escape.rst",
    ],
    interludes=itertools.repeat(interlude)
)

schedule.extend((ray, justin))
