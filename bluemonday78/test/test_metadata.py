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

from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import SceneScript

class LocationMatcher(Matcher):

    def options(self, data):
        arc = data.get("arc", None)
        yield from (
            i for i in self.folders
            if arc is not None and i.metadata.get("arc") == arc
        )

class MetadataTests(unittest.TestCase):

    def test_change_location(self):
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
        matcher = LocationMatcher(folders)

        rv = list(matcher.options({"arc": "a_11"}))
        self.assertEqual(1, len(rv), rv)
        self.assertEqual("a_11", rv[0].metadata["arc"])

