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

import collections
from collections.abc import Callable
import enum
import sys
import unittest

from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer
from turberfield.dialogue.types import EnumFactory
from turberfield.utils.misc import group_by_type
from turberfield.utils.assembly import Assembly

from bluemonday78.matcher import MultiMatcher
import bluemonday78.story
from bluemonday78.story import Spot
from bluemonday78.types import Location
from bluemonday78.types import Narrator


class TimeSpanTests(unittest.TestCase):

    def test_seconds(self):
        start, span = MultiMatcher.parse_timespan("20191108173004")
        self.assertEqual(2019, start.year)
        self.assertEqual(11, start.month)
        self.assertEqual(8, start.day)
        self.assertEqual(17, start.hour)
        self.assertEqual(30, start.minute)
        self.assertEqual(4, start.second)
        self.assertEqual(1, span.seconds)

    def test_minutes(self):
        start, span = MultiMatcher.parse_timespan("201911081730")
        self.assertEqual(2019, start.year)
        self.assertEqual(11, start.month)
        self.assertEqual(8, start.day)
        self.assertEqual(17, start.hour)
        self.assertEqual(30, start.minute)
        self.assertEqual(60, span.seconds)

    def test_hours(self):
        start, span = MultiMatcher.parse_timespan("2019110817")
        self.assertEqual(2019, start.year)
        self.assertEqual(11, start.month)
        self.assertEqual(8, start.day)
        self.assertEqual(17, start.hour)
        self.assertEqual(3600, span.seconds)

    def test_days(self):
        start, span = MultiMatcher.parse_timespan("20191108")
        self.assertEqual(2019, start.year)
        self.assertEqual(11, start.month)
        self.assertEqual(8, start.day)
        self.assertEqual(1, span.days)


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.ensemble = bluemonday78.story.ensemble()

    def test_search_none(self):
        rv = set(bluemonday78.story.search(
            self.ensemble, Narrator
        ))
        self.assertFalse(rv)

    def test_search_many(self):
        rv = set(bluemonday78.story.search(
            self.ensemble, Location
        ))
        self.assertEqual(5, len(rv))

    def test_search_single(self):
        rv = set(bluemonday78.story.search(
            self.ensemble, Location,
            label="Visiting Suite"
        ))
        self.assertEqual(1, len(rv))

    def test_search_empty(self):
        rv = set(bluemonday78.story.search(
            self.ensemble, Narrator,
            label="Visiting Suite"
        ))
        self.assertFalse(rv)

    def test_search_attribute(self):
        rv = set(bluemonday78.story.search(
            self.ensemble,
            label="Visiting Suite"
        ))
        self.assertEqual(1, len(rv))


class SequenceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ensemble = bluemonday78.story.ensemble(
            bluemonday78.story.build_story("Mr Likely Story")
        )
        cls.characters = {
            k.__name__: v for k, v in group_by_type(cls.ensemble).items()
        }
        cls.performer = Performer(
            list(bluemonday78.story.prepare_folders()),
            cls.ensemble
        )

    def setUp(self):
        self.assertEqual(16, len(self.ensemble))
        (self.folder, self.index, self.script, self.selection,
         self.interlude) = self.performer.next(
            self.performer.folders, self.ensemble, strict=True, roles=1
        )

    def tearDown(self):
        if isinstance(self.interlude, Callable):
            metadata = self.interlude(
                self.folder, self.index,
                self.ensemble, self.performer.folders
            )
            self.assertIn(metadata, (None, self.folder.metadata))

    def test_001(self):
        self.assertEqual(
            Spot.w12_ducane_prison_wing,
            next(
                i for i in self.performer.ensemble
                if getattr(i, "_name", None) == "Mr Martin Sheppey"
            ).get_state(Spot),
            self.performer.ensemble
        )
        self.assertEqual(
            Spot.w12_ducane_prison_wing,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("step_forward.rst"))
        self.assertEqual(4, len(self.performer.shots))
        self.assertEqual(
            "ray joins them on the balcony",
            self.performer.shots[-1].name
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Narrator"][0].get_state(Spot)
        )

    def test_002(self):
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

        self.assertFalse(self.performer.stopped)
        folder, index, script, selection, interlude = self.performer.next(
            self.performer.folders, self.performer.ensemble
        )
        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("getting_here.rst"))
        self.assertEqual(4, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

    def test_003(self):
        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("hows_work.rst"))
        self.assertEqual(5, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

    def test_004(self):
        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("these_keys.rst"))
        self.assertEqual(6, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )


class AssemblyTests(unittest.TestCase):

    class ForeignState(EnumFactory, enum.Enum):
        friendly = 0
        hostile = 1

    def test_assembly(self):
        narrator = bluemonday78.story.build_story("Mr Dick Turpin")
        ensemble = bluemonday78.story.ensemble(narrator)
        text = Assembly.dumps(ensemble)
        clone = Assembly.loads(text)

        self.assertEqual(
            set(group_by_type(ensemble).keys()),
            set(group_by_type(clone).keys()),
            "Check all ensemble classes permit re-assembly (DataObject)"
        )

    def test_ready_narrator_01(self):
        Assembly.register(AssemblyTests.ForeignState)
        narrator = bluemonday78.story.build_story("Mr Dick Turpin").set_state(AssemblyTests.ForeignState.hostile)
        self.assertTrue(hasattr(narrator, "memories"))
        self.assertIsInstance(narrator.memories, collections.deque)
        narrator.memories.extend(range(4))
        self.assertEqual(197801160800, narrator.state)
        self.assertEqual(4, len(narrator.memories))
        self.assertEqual(3, len(narrator._states))

        text = Assembly.dumps(narrator)
        clone = Assembly.loads(text)
        self.assertEqual(narrator.id, clone.id)
        self.assertTrue(hasattr(clone, "memories"))
        self.assertIsInstance(clone.memories, list)
        self.assertEqual(4, len(clone.memories))
        self.assertEqual(3, len(narrator._states))

        # Check state transfer
        self.assertEqual(197801160800, clone.state)
        clone.state = 0

        result = bluemonday78.story.build_story(
            clone.name,
            id=None,
            memories=clone.memories,
            _states=clone._states
        )
        self.assertNotEqual(clone.id, result.id)
        self.assertTrue(hasattr(result, "memories"))
        self.assertIsInstance(result.memories, collections.deque)
        self.assertEqual(4, len(result.memories))
        self.assertEqual(0, result.state)
        self.assertEqual(3, len(result._states))
        self.assertEqual(AssemblyTests.ForeignState.hostile, result.get_state(AssemblyTests.ForeignState))
