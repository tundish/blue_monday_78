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

from bluemonday78.matcher import PathwayMatcher


class MatcherTests(unittest.TestCase):

    def test_match_by_arc(self):
        folders = [
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
                        ("w12_ducane", "prison"),
                    ))
                },
                {
                    "arc": "a_10",
                    "pathways": frozenset((
                        ("w12_ducane", "prison"),
                    ))
                },
                {
                    "arc": "a_11",
                    "pathways": frozenset((
                        ("w12_ducane", "prison"),
                    ))
                },
            ]
        ]
        matcher = PathwayMatcher(folders)

        rv = list(matcher.options({"arc": "a_11"}))
        self.assertEqual(1, len(rv), rv)
        self.assertEqual("a_11", rv[0].metadata["arc"])

