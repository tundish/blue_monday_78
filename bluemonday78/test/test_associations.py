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

from bluemonday78.associations import Associations
from bluemonday78.story import Location

class AssociationTests(unittest.TestCase):

    def setUp(self):
        self.associations = Associations()

    def test_register_none(self):
        self.associations.register(
            None,
            Location(id=1, label="Wormwood Scrubs prison wing"),
            Location(id=2, label="Wormwood Scrubs reception"),
        )
        lookup = self.associations.lookup
        self.assertTrue([i for i in lookup if i.id == 1])
        self.assertTrue([i for i in lookup if i.id == 2])
        self.assertNotIn(
            None,
            lookup[next(i for i in lookup if i.id == 1)],
        )

    def test_register_search(self):
        assoc = self.associations.register(
            None,
            Location(id=1, label="Wormwood Scrubs prison wing"),
            Location(id=2, label="Wormwood Scrubs reception"),
        )
        lookup = self.associations.lookup
        self.assertTrue([i for i in lookup if i.id == 1])
        self.assertTrue([i for i in lookup if i.id == 2])
