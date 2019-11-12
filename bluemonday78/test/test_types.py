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

import unittest

from bluemonday78.types import Player
from bluemonday78.types import Spot


class CreationTests(unittest.TestCase):

    def test_keys(self):
        state = Spot.factory(name="w12_goldhawk_cafe")
        self.assertEqual(Spot.w12_goldhawk_cafe, state)

    def test_player(self):
        player = Player(name="Test")
        self.assertTrue(hasattr(player, "id"))
        self.assertTrue(hasattr(player, "name"))
