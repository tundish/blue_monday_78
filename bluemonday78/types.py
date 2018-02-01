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

import enum

from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful


class Drama(EnumFactory, enum.Enum):
    inactive = 0
    active = 1

class Mission(EnumFactory, enum.Enum):
    travel = "travel"
    empty = "empty"

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d"
    w12_ducane_prison_visiting = "gcpv4d252v5y"
    w12_ducane_prison_release = "gcpv4d1qmdzb"
    w12_ducane_prison_wing = "gcpv4d675t07"
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
