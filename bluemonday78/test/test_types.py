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

from bluemonday78.types import Phrase
from turberfield.dialogue.types import Stateful

class PhraseTests(unittest.TestCase):

    def test_class_name(self):
        self.assertEqual(
            "Thats25HoursWorkAllWasted",
            Phrase.class_name("That's 2.5 hours' work __all__   wasted!")
        )

    def test_build(self):
        cls = Phrase.build("these are testing times")
        self.assertTrue(issubclass(cls, Stateful))
        obj = cls.instance()
        self.assertIsInstance(obj, Stateful)
