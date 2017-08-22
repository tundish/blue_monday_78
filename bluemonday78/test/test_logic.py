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


class MockHandler(TerminalHandler):

    def __init__(self, folder, references):
        self.folder = folder
        self.references = references
        self.calls = 0
        self.visits = Counter()
        try:
            super().__init__(terminal=None, pause=0, dwell=0)
        except UserWarning:
            # NOTE: dev on 12.04
            pass

    def handle_scene(self, obj):
        return obj

    def handle_shot(self, obj):
        return obj

    def handle_property(self, obj):
        if obj.object is not None:
            try:
                setattr(obj.object, obj.attr, obj.val)
            except AttributeError as e:
                self.log.error(". ".join(getattr(e, "args", e) or e))
        return obj


class SceneTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ensemble = ensemble()
        cls.schedule = copy.deepcopy(schedule)
        cls.characters = {
            typ.__name__: next(i for i in cls.ensemble if isinstance(i, typ))
            for typ in (Barman, Hipster, Player, Narrator, PrisonOfficer)
        }
        cls.folder = next(i for i in cls.schedule if i.paths == ray.paths)
        cls.state = Presenter.new_state(cls.folder)
        cls.handler = MockHandler(cls.folder, cls.ensemble)

    @classmethod
    def branch_folder(cls, folder, reload=False):
        if reload or folder is not cls.folder:
            cls.state = Presenter.new_state(folder)
            cls.folder = folder

    @staticmethod
    def run_script(folder, script, references, handler):
        strict = any(i.paths == folder.paths for i in plotlines)
        n = 0
        for shot, item in run_through(
            script, references, strict=strict
        ):
            n += 1
            list(handler(shot, loop=None))
            list(handler(item, loop=None))
        return n

    def test_001(self):
        self.assertEqual(
            Spot.w12_ducane_prison,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_ducane_prison_visiting,
            self.characters["PrisonOfficer"].get_state(Spot)
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780116, self.characters["PrisonOfficer"].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["PrisonOfficer"].get_state(Spot)
        )
        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(justin.paths, folder.paths)
        self.branch_folder(folder)

    def test_002(self):
        self.assertEqual(19780116, self.characters["Hipster"].get_state())
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"].get_state(Spot)
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780117, self.characters["Hipster"].get_state())
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Hipster"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(local.paths, folder.paths)
        self.branch_folder(folder)

    def test_003(self):
        self.assertEqual(19780116, self.characters["Narrator"].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"].get_state(Spot)
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780117, self.characters["Narrator"].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(ray.paths, folder.paths)
        self.branch_folder(folder)

    def test_004(self):
        self.assertEqual(19780117, self.characters["Narrator"].get_state())
        self.assertEqual(
            Spot.w12_ducane_prison,
            self.characters["Narrator"].get_state(Spot)
        )
        self.assertEqual(
            Spot.w12_ducane_prison_release,
            self.characters["Player"].get_state(Spot)
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780117, self.characters["Narrator"].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(justin.paths, folder.paths)
        self.branch_folder(folder)

    def test_005(self):
        self.assertEqual(19780117, self.characters["Narrator"].get_state())
        self.assertEqual(19780117, self.characters["Hipster"].get_state())
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Narrator"].get_state(Spot)
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780117, self.characters["Narrator"].get_state())
        self.assertEqual(19780118, self.characters["Hipster"].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(local.paths, folder.paths)
        self.branch_folder(folder)

    def test_006(self):
        n = 0
        while not n:
            index, script, interlude = next(self.state)
            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(local.paths, self.folder.paths)
        self.assertEqual(0, index)

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(19780118, self.characters["Hipster"].get_state())
        self.assertEqual(19780118, self.characters["Narrator"].get_state())
        self.assertEqual(19780118, self.characters["PrisonOfficer"].get_state())
        self.assertEqual(ray.paths, folder.paths)
        self.branch_folder(folder)

    def test_007(self):
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(19780118, self.characters["Hipster"].get_state())

        n = 0
        while not n:
            try:
                index, script, interlude = next(self.state)
            except StopIteration:
                # No selection from ray
                folder = interlude(
                    self.folder, index,
                    self.ensemble, self.schedule,
                    phrase=None
                )
                self.branch_folder(folder)

            with script as dialogue:
                selection = dialogue.select(self.ensemble, roles=1)

            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780118, self.characters["Narrator"].get_state())
        self.assertEqual(justin.paths, self.folder.paths)
        self.assertEqual(2, index)
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(19780118, self.characters["Hipster"].get_state())

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(19780118, self.characters["Narrator"].get_state())
        self.assertEqual(local.paths, folder.paths)
        self.branch_folder(folder)

    @unittest.skip("abandoned branching dialogue.")
    def test_008(self):
        self.assertEqual(
            Attitude.neutral,
            self.characters["Barman"].get_state(Attitude)
        )

        n = 0
        while not n:
            try:
                index, script, interlude = next(self.state)
            except StopIteration:
                folder = interlude(
                    self.folder, index,
                    self.ensemble, self.schedule,
                    phrase=phrases[0]
                )

                self.assertEqual(
                    Attitude.grumpy,
                    self.characters["Barman"].get_state(Attitude)
                )
                self.branch_folder(folder)

            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(3, n)  # One each of script, shot, line
        self.assertEqual(
            Attitude.neutral,
            self.characters["Barman"].get_state(Attitude)
        )
        self.assertEqual(local.paths, folder.paths)
        self.branch_folder(folder, reload=True)

    @unittest.skip("abandoned branching dialogue.")
    def test_009(self):
        self.assertEqual(
            19780118,
            self.characters["Hipster"].get_state()
        )

        n = 0
        while not n:
            index, script, interlude = next(self.state)

            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=phrases[1]
        )
        self.assertEqual(
            19780119,
            self.characters["Hipster"].get_state()
        )
        self.assertEqual(justin.paths, folder.paths)
        self.branch_folder(folder)

    def test_010(self):
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(19780118, self.characters["Hipster"].get_state())

        n = 0
        while not n:
            try:
                index, script, interlude = next(self.state)
            except StopIteration:
                # No selection from ray
                folder = interlude(
                    self.folder, index,
                    self.ensemble, self.schedule,
                    phrase=None
                )
                self.branch_folder(folder)

            with script as dialogue:
                selection = dialogue.select(self.ensemble, roles=1)

            n = self.run_script(
                self.folder, script, self.ensemble,
                self.handler
            )

        self.assertEqual(19780119, self.characters["Hipster"].get_state())
        self.assertEqual(justin.paths, self.folder.paths)
        self.assertEqual(1, index)
        self.assertEqual(
            Spot.w12_goldhawk_tavern,
            self.characters["Player"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Player"].get_state(Spot)
        )
        self.assertEqual(19780119, self.characters["PrisonOfficer"].get_state())
        self.assertEqual(local.paths, folder.paths)
        self.branch_folder(folder)
