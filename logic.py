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

import enum

from turberfield.dialogue.types import EnumFactory
from turberfield.utils.assembly import Assembly

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison_approach = "gcpv4d2dm6v2"
    w12_goldhawk_cafe_approach = "gcpufzg2512x"
    w12_goldhawk_tavern_approach = "gcpufzbd8x5d"
    w12_latimer_arches_approach = "gcpv4cxb3dh4"
