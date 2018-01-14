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

import unittest

from bluemonday78.logic import Associations
from bluemonday78.logic import Location
from bluemonday78.logic import Via

class AssociationTests(unittest.TestCase):

    def tearDown(self):
        Associations.clear()

    def test_ensemble(self):
        Associations.register(
            Via.bidir,
            Location(label="Wormwood Scrubs prison wing"),
            Location(label="Wormwood Scrubs reception"),
        )
        rv = Associations.ensemble("wing")
        self.assertIsInstance(rv, Location)
        print(Associations.ensemble())
