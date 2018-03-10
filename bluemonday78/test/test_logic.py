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
import sys
import unittest

from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer
from turberfield.utils.misc import group_by_type

from bluemonday78.logic import associations
from bluemonday78.logic import ray
from bluemonday78.logic import Spot
from bluemonday78.types import Travel
from bluemonday78.types import Visibility

class RaySequenceTests(unittest.TestCase):

    def make_association(obj, associations):
        if isinstance(obj, Model.Memory) and obj.object:
            associations.register(obj.state, obj.subject, obj.object)

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
        self.assertEqual(17, len(self.ensemble))
        (self.folder, self.index, self.script, self.selection,
         self.interlude) = self.performer.next(
            self.dialogue, self.ensemble, strict=True, roles=1
        )

    def tearDown(self):
        print("Teardown", self.folder.paths[self.index], file=sys.stderr)
        print("Interlude", self.interlude, file=sys.stderr)
        if isinstance(self.interlude, Callable):
            branch = self.interlude(
                self.folder, self.index, self.ensemble, self.dialogue
            )
            self.assertIn(branch, (self.folder, None))

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
        self.assertTrue(self.performer.script.fP.endswith("step_forward.rst"))
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
        self.assertTrue(self.performer.script.fP.endswith("getting_here.rst"))
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
        self.assertTrue(self.performer.script.fP.endswith("hows_work.rst"))
        self.assertEqual(3, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(197801160820, self.characters["PrisonVisitor"][0].get_state())

    def test_004(self):
        self.assertEqual(197801160820, self.characters["PrisonVisitor"][0].get_state())

        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("these_keys.rst"))
        self.assertEqual(4, len(self.performer.shots))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(197801160830, self.characters["PrisonVisitor"][0].get_state())

    def test_005(self):
        self.assertEqual(197801160830, self.characters["PrisonVisitor"][0].get_state())
        self.assertEqual(197801160800, self.characters["PrisonOfficer"][0].get_state())

        self.assertEqual(
            Visibility.hidden,
            self.characters["NoteBook"][0].get_state(Visibility)
        )
        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("pocket_fax.rst"))
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
        self.assertEqual(
            Visibility.visible,
            self.characters["NoteBook"][0].get_state(Visibility)
        )

    def test_006(self):
        self.assertEqual(197801160810, self.characters["PrisonOfficer"][0].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertTrue(self.performer.script.fP.endswith("admin.rst"))
        self.assertEqual(7, len(self.performer.shots))
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

        for obj in self.performer.run():
            RaySequenceTests.make_association(obj, self.asscns)
        self.assertTrue(self.performer.script.fP.endswith("frankly.rst"))
        self.assertEqual(7, len(self.performer.shots))
        self.assertEqual(
            "guards' office",
            self.performer.shots[-1].scene
        )
        self.assertEqual(
            "ray does the paperwork",
            self.performer.shots[-1].name,
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            197801160830,
            self.characters["PrisonOfficer"][0].get_state()
        )

        hero = self.characters["Player"][0]
        location = self.asscns.search(label="Wormwood Scrubs visiting").pop()
        self.assertIn(location, self.asscns.lookup[hero][Travel.intention])

    def test_008(self):
        hero = self.characters["Player"][0]
        self.assertEqual(
            Spot.w12_ducane_prison_visiting,
            hero.get_state(Spot)
        )

        self.assertEqual(
            197801160830,
            self.characters["PrisonVisitor"][0].get_state()
        )
        self.assertEqual(
            197801160830,
            self.characters["PrisonOfficer"][0].get_state()
        )

        list(self.performer.run())
        self.assertEqual(8, len(self.performer.shots))
        self.assertTrue(self.performer.script.fP.endswith("transfer.rst"))
        self.assertEqual(
            "in the visiting suite",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

    def test_009(self):
        self.assertEqual(
            197801160830,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(9, len(self.performer.shots))
        self.assertTrue(self.performer.script.fP.endswith("escape.rst"))
        self.assertEqual(
            "getting out",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            197801160830,
            self.characters["PrisonOfficer"][0].get_state()
        )

    def test_010(self):
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"][0].get_state(Spot)
        )
