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

from collections.abc import Callable
import copy
import unittest

from turberfield.dialogue.performer import Performer
from turberfield.utils.misc import group_by_type

from bluemonday78.logic import associations
from bluemonday78.logic import ray
from bluemonday78.logic import Spot
from bluemonday78.logic import schedule

class RaySequenceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.asscns = associations()
        cls.ensemble = cls.asscns.ensemble()
        cls.dialogue = [copy.deepcopy(ray)]
        cls.characters = {
            k.__name__: v for k, v in group_by_type(cls.ensemble).items()
        }
        cls.performer = Performer(cls.dialogue, cls.ensemble)

    def setUp(self):
        self.assertEqual(15, len(self.ensemble))
        (self.folder, self.index, self.script, self.selection,
         self.interlude) = self.performer.next(
            self.dialogue, self.ensemble, strict=True, roles=1
        )

    def tearDown(self):
        if isinstance(self.interlude, Callable):
            branch = self.interlude(
                self.folder, self.index, self.ensemble, self.dialogue
            )
            self.assertIs(self.folder, branch)

    def test_001(self):
        self.assertEqual(
            Spot.w12_ducane_prison_wing,
            self.asscns.search(_name="Mr Martin Sheppey").pop().get_state(Spot)
        )
        self.assertEqual(
            197801160800,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_wing,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(1, len(self.performer.shots))
        self.assertEqual(
            "ray is on the landing",
            self.performer.shots[-1].name
        )

        self.assertEqual(
            197801160800,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_ducane_prison_visiting,
            self.characters["Player"][0].get_state(Spot)
        )

    def test_002(self):
        self.assertEqual(
            197801160800,
            self.characters["PrisonVisitor"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

        self.assertFalse(self.performer.stopped)
        folder, index, script, selection, interlude = self.performer.next(
            self.performer.folders, self.performer.ensemble
        )
        list(self.performer.run())
        self.assertEqual(2, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            197801160810,
            self.characters["PrisonVisitor"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

    def test_003(self):
        self.assertEqual(197801160810, self.characters["PrisonVisitor"][0].get_state())

        list(self.performer.run())
        self.assertEqual(3, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(197801160820, self.characters["PrisonVisitor"][0].get_state())

    def test_004(self):
        self.assertEqual(197801160820, self.characters["PrisonVisitor"][0].get_state())

        list(self.performer.run())
        self.assertEqual(4, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(197801160830, self.characters["PrisonVisitor"][0].get_state())

    def test_005(self):
        self.assertEqual(197801160830, self.characters["PrisonVisitor"][0].get_state())
        self.assertEqual(197801160800, self.characters["PrisonOfficer"][0].get_state())

        list(self.performer.run())
        self.assertEqual(6, len(self.performer.shots))
        self.assertEqual(
            "guards' office",
            self.performer.shots[-1].scene
        )

        self.assertEqual(197801160810, self.characters["PrisonOfficer"][0].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )

    def test_006(self):
        self.assertEqual(197801160810, self.characters["PrisonOfficer"][0].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(8, len(self.performer.shots))
        self.assertEqual(
            "guards' office",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            197801160800,
            self.characters["Player"][0].get_state()
        )
        self.assertEqual(
            197801160820,
            self.characters["PrisonOfficer"][0].get_state()
        )

    def test_007(self):
        self.assertEqual(
            197801160820,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(9, len(self.performer.shots))
        self.assertEqual(
            "getting out",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            197801160830,
            self.characters["PrisonOfficer"][0].get_state()
        )

    def test_008(self):
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(13, len(self.performer.shots))
        self.assertEqual(
            "a chance encounter",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

        self.assertEqual(
            19780119,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            19780119,
            self.characters["PrisonOfficer"][0].get_state()
        )
