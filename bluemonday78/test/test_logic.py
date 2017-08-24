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

from collections import Counter
from collections.abc import Callable
import copy
import unittest

from turberfield.dialogue.handlers import TerminalHandler
from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.player import run_through
from turberfield.utils.misc import group_by_type

from bluemonday78.logic import Attitude
from bluemonday78.logic import blue_monday
from bluemonday78.logic import Barman
from bluemonday78.logic import Character
from bluemonday78.logic import Hipster
from bluemonday78.logic import MatchMaker
from bluemonday78.logic import Narrator
from bluemonday78.logic import phrases
from bluemonday78.logic import Player
from bluemonday78.logic import Prisoner
from bluemonday78.logic import PrisonOfficer
from bluemonday78.logic import PrisonVisitor
from bluemonday78.logic import Spot
from bluemonday78.logic import justin, local, ray
from bluemonday78.logic import ensemble, plotlines, schedule
from bluemonday78.main import Presenter
from bluemonday78.performer import Performer


class SceneTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ensemble = ensemble()
        cls.schedule = copy.deepcopy(schedule)
        cls.characters = {
            k.__name__: v for k, v in group_by_type(cls.ensemble).items()
        }
        cls.performer = Performer(cls.schedule, cls.ensemble)

    def test_001(self):
        self.assertEqual(
            Spot.w12_ducane_prison_visiting,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            19780116,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_visiting,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(6, len(self.performer.shots))
        self.assertEqual(
            "ray does the paperwork",
            self.performer.shots[-1].name
        )

        self.assertEqual(
            19780116,
            self.characters["PrisonOfficer"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"][0].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Narrator"][0].get_state(Spot)
        )

    def test_002(self):
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            19780116,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

        self.assertFalse(self.performer.stopped)
        script, selection = self.performer.next(self.performer.folders, self.performer.ensemble)
        list(self.performer.run())
        self.assertEqual(7, len(self.performer.shots))
        self.assertEqual(
            "sorrows",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            19780117,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"][0].get_state(Spot)
        )

    def test_003(self):
        self.assertEqual(19780116, self.characters["Narrator"][0].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(8, len(self.performer.shots))
        self.assertEqual(
            "addison arches",
            self.performer.shots[-1].scene
        )

        self.assertEqual(19780117, self.characters["Narrator"][0].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Narrator"][0].get_state(Spot)
        )

    def test_004(self):
        self.assertEqual(19780117, self.characters["Narrator"][0].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Narrator"][0].get_state(Spot)
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
            19780117,
            self.characters["Narrator"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Narrator"][0].get_state(Spot)
        )

        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )

    def test_005(self):
        self.assertEqual(
            19780117,
            self.characters["Narrator"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            19780117,
            self.characters["Hipster"][0].get_state()
        )

        list(self.performer.run())
        self.assertEqual(10, len(self.performer.shots))
        self.assertEqual(
            "anguish",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            19780117,
            self.characters["Narrator"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            19780118,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )

    def test_006(self):
        self.assertEqual(
            19780117,
            self.characters["Narrator"][0].get_state()
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )

        list(self.performer.run())
        self.assertEqual(11, len(self.performer.shots))
        self.assertEqual(
            "addison arches",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            19780118,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            19780118,
            self.characters["Narrator"][0].get_state()
        )
        self.assertEqual(
            19780118,
            self.characters["PrisonOfficer"][0].get_state()
        )

    def test_007(self):
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            19780118,
            self.characters["Hipster"][0].get_state()
        )
        self.assertEqual(
            19780118,
            self.characters["Narrator"][0].get_state()
        )

        list(self.performer.run())
        self.assertEqual(12, len(self.performer.shots))
        self.assertEqual(
            "desparation",
            self.performer.shots[-1].scene
        )

        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"][0].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"][0].get_state(Spot)
        )
        self.assertEqual(
            19780118,
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
