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

import collections
import unittest

from bluemonday78.logic import MatchMaker


class MatchMakerTests(unittest.TestCase):

    def setUp(self):
        self._lookup, MatchMaker.lookup = MatchMaker.lookup, collections.defaultdict(list)

    def tearDown(self):
        MatchMaker.lookup = self._lookup

    def test_tokenize(self):
        self.assertEqual(
            ("one", "two", "hree", "four"),
            MatchMaker.tokenize("oNe Two 3hree Four!")
        )

    def test_match(self):
        phrase = MatchMaker.Phrase("Thank you.", ["thanks", "cheers"])
        MatchMaker.register(phrase)
        self.assertEqual(2, len(MatchMaker.words()))
        rv = next(MatchMaker.match("Thanks!"), None)
        self.assertEqual(phrase, rv)

    def test_match_surplus(self):
        phrase = MatchMaker.Phrase("Thank you.", ["thanks", "cheers"])
        MatchMaker.register(phrase)
        rv = next(MatchMaker.match("Thanks a lot!"), None)
        self.assertEqual(phrase, rv)
