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

import datetime
import enum
import string

from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful
from turberfield.utils.assembly import Assembly


@enum.unique
class Look(EnumFactory, enum.Enum):
    youth = 1
    mug = 2
    punter = 3
    yuppie = 4
    hipster= 5
    face = 6
    veteran = 7


@enum.unique
class Mode(EnumFactory, enum.Enum):
    guardian = 1
    healer = 2
    mage = 3
    thief = 4


@enum.unique
class Trade(EnumFactory, enum.Enum):
    singer = 1
    innkeeper = 2
    merchant = 3
    politician = 4


class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison_release = ("w12_ducane", "prison_office")
    w12_ducane_prison_visiting = ("w12_ducane", "prison_visiting")
    w12_ducane_prison_wing = ("w12_ducane", "prison_wing")
    w12_goldhawk_cafe = ("w12_latimer", "cafe")
    w12_goldhawk_tavern = ("w12_latimer", "goldhawk_tavern")
    w12_latimer_lockup = ("w12_latimer", "lockup")
    w12_latimer_arches = ("w12_latimer", "arches")


class Character(Stateful, Persona): pass
class Location(Stateful, DataObject): pass


class Narrator(Stateful, DataObject):

    state_format = "%Y%m%d%H%M"

    @staticmethod
    def parse_timespan(text: str):
        formats = {
            8: ("%Y%m%d", datetime.timedelta(days=1)),
            10: ("%Y%m%d%H", datetime.timedelta(hours=1)),
            12: ("%Y%m%d%H%M", datetime.timedelta(minutes=1)),
            14: ("%Y%m%d%H%M%S", datetime.timedelta(seconds=1)),
        }
        if len(text) not in formats and min(formats) < len(text) < max(formats):
            text = text + "0"
            mult = 10
        else:
            mult = 1
        try:
            format_string, span = formats[len(text)]
        except KeyError:
            return text, None
        else:
            return datetime.datetime.strptime(text, format_string), mult * span

    @property
    def clock(self):
        text = str(self.get_state(int))
        ts, span = self.parse_timespan(text)
        return ts

    @clock.setter
    def clock(self, hours=1):
        try:
            td = datetime.timedelta(hours=hours)
            ts = self.clock + td
            self.set_state(int(ts.strftime(self.state_format)))
        finally:
            return self.clock


Assembly.register(Look, Mode, Trade, Spot, Character, Location, Narrator)
