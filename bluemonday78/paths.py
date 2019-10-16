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

from turberfield.dialogue.types import Player
from bluemonday78.types import Spot

class GoldenPath:

    def locate_to_karen(folder, index, references, *args, **kwargs):
        player = next(i for i in references if isinstance(i, Player))
        player.set_state(Spot.w12_ducane_prison_visiting)
        return folder.metadata

    def locate_to_ray(folder, index, references, *args, **kwargs):
        player = next(i for i in references if isinstance(i, Player))
        player.set_state(Spot.w12_ducane_prison_release)
        return folder.metadata

    def stop(folder, index, references, *args, **kwargs):
        return None
