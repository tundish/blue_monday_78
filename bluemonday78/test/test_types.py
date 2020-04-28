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
import unittest

from bluemonday78.story import build_narrator
from bluemonday78.types import Narrator
from bluemonday78.types import Spot


class NarratorTests(unittest.TestCase):

    def test_creation(self):
        narrator = Narrator()
        self.assertTrue(hasattr(narrator, "id"))

    def test_clock_getter(self):
        narrator = build_narrator()
        self.assertEqual(datetime.datetime(1978, 1, 16, 8), narrator.clock)

    def test_clock_setter(self):
        narrator = build_narrator()
        self.assertEqual(datetime.datetime(1978, 1, 16, 8), narrator.clock)
        self.assertEqual(197801160800, narrator.state)

        narrator.clock = 1
        self.assertEqual(datetime.datetime(1978, 1, 16, 9), narrator.clock)
        self.assertEqual(197801160900, narrator.state)

        narrator.clock = 3
        self.assertEqual(datetime.datetime(1978, 1, 16, 12), narrator.clock)
        self.assertEqual(197801161200, narrator.state)

        narrator.clock = 12
        self.assertEqual(datetime.datetime(1978, 1, 17, 0), narrator.clock)
        self.assertEqual(197801170000, narrator.state)

        # Not a good idea
        narrator.set_state(7)
        self.assertEqual('7', narrator.clock)
        self.assertEqual(7, narrator.state)

        narrator.clock = 1
        self.assertEqual('7', narrator.clock)
        self.assertEqual(7, narrator.state)


class SpotTests(unittest.TestCase):

    def test_keys(self):
        state = Spot.factory(name="w12_goldhawk_cafe")
        self.assertEqual(Spot.w12_goldhawk_cafe, state)
