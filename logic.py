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

import datetime
import enum
import itertools

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Stateful
from turberfield.utils.assembly import Assembly

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d2dm6v2"
    w12_goldhawk_cafe = "gcpufzg2512x"
    w12_goldhawk_tavern = "gcpufzbd8x5d"
    w12_latimer_arches = "gcpv4cxb3dh4"

class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass
class PrisonOfficer(Stateful, Persona): pass

blue_monday = datetime.date(1978, 1, 16)

ensemble = [
    Barman(name="Barry Latimer").set_state(Spot.w12_goldhawk_tavern),
    Hipster(name="Justin Cornelis Delcroix").set_state(Spot.w12_goldhawk_tavern),
]

references = ensemble + [Spot]

justin = SceneScript.Folder(
    pkg=__name__,
    description="Justin Delcroix has just got the sack.",
    metadata=[blue_monday],
    paths=["justin_19780116_fired/sorrows.rst"],
    interludes=itertools.repeat(None)
)

ray = SceneScript.Folder(
    pkg=__name__,
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=["ray_19780116_retires/admin.rst"],
    interludes=itertools.repeat(None)
)
