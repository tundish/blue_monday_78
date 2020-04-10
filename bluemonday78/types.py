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
from turberfield.dialogue.types import Player
from turberfield.dialogue.types import Stateful
from turberfield.utils.assembly import Assembly


@enum.unique
class Alignment(EnumFactory, enum.Enum):
    healer = 0
    guardian = 1
    thief = 2
    merchant = 3
    bard = 4
    politician = 5


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


# TODO: Get rid
class Page(EnumFactory, enum.Enum):
    closed = 0
    opened = 1
    marked = 2

# TODO:: Get rid
class NoteBook(Stateful, DataObject): pass
class PrisonOfficer(Stateful, Persona): pass
class Prisoner(Stateful, Persona): pass
class PrisonVisitor(Stateful, Persona): pass
class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass


Assembly.register(
    Narrator, Spot, PrisonOfficer, Prisoner, PrisonVisitor, Barman, Hipster, Character, Location,
    NoteBook, Page, Player
)
