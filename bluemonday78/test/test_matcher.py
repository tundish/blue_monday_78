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

from turberfield.dialogue.model import SceneScript

from bluemonday78.matcher import MultiMatcher


class MatcherTests(unittest.TestCase):

    def setUp(self):
        self.folders = [
            SceneScript.Folder(
                pkg=None,
                description=None,
                paths=None,
                interludes=None,
                metadata=i
            )
            for i in [
                {
                    "arc": "a_01",
                    "pathways": frozenset((
                        ("w12_latimer", "lockup"),
                    ))
                },
                {
                    "arc": "a_10",
                    "pathways": frozenset((
                        ("w12_latimer", "tavern"),
                    ))
                },
                {
                    "arc": "a_11",
                    "pathways": frozenset((
                        ("w12_latimer", "lockup"),
                        ("w12_latimer", "tavern"),
                    ))
                },
            ]
        ]

    def test_match_by_arc(self):
        matcher = MultiMatcher(self.folders)

        rv = list(matcher.options({"arc": "a_11"}))
        self.assertEqual(1, len(rv), rv)
        self.assertEqual("a_11", rv[0].metadata["arc"])

    def test_match_by_pathway(self):
        matcher = MultiMatcher(self.folders)

        rv = list(matcher.options(
            {"pathways": set([("w12_latimer", "lockup")])}
        ))
        self.assertEqual(2, len(rv), rv)
        self.assertEqual("a_01", rv[0].metadata["arc"])
        self.assertEqual("a_11", rv[1].metadata["arc"])

