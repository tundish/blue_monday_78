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

import enum
import string

from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful
from turberfield.utils.assembly import Assembly


@enum.unique
class Fit(EnumFactory, enum.Enum):
    bard = 1
    guardian = 2
    healer = 3
    innkeeper = 4
    merchant = 5
    politician = 6
    thief = 7


class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison_release = ("w12_ducane", "prison_office")
    w12_ducane_prison_visiting = ("w12_ducane", "prison_visiting")
    w12_ducane_prison_wing = ("w12_ducane", "prison_wing")
    w12_goldhawk_cafe = ("w12_latimer", "cafe")
    w12_goldhawk_tavern = ("w12_latimer", "tavern")
    w12_latimer_lockup = ("w12_latimer", "lockup")
    w12_latimer_arches = ("w12_latimer", "arches")


class Character(Stateful, Persona): pass
class Location(Stateful, DataObject): pass
class Narrator(Stateful, DataObject): pass


Assembly.register(Fit, Spot, Character, Location, Narrator)
