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

from bluemonday78.logic import blue_monday
from bluemonday78.logic import Barman
from bluemonday78.logic import Character
from bluemonday78.logic import Hipster
from bluemonday78.logic import MatchMaker
from bluemonday78.logic import Narrator
from bluemonday78.logic import Player
from bluemonday78.logic import Prisoner
from bluemonday78.logic import PrisonOfficer
from bluemonday78.logic import PrisonVisitor
from bluemonday78.logic import Spot
from bluemonday78.main import Presenter
from bluemonday78.logic import justin, local, ray
from bluemonday78.logic import ensemble, plotlines, schedule


class MockHandler(TerminalHandler):

    def __init__(self, folder, references):
        self.folder = folder
        self.references = references
        self.calls = 0
        self.visits = Counter()
        super().__init__(terminal=None, pause=0, dwell=0)

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
            for typ in (Hipster, Player, Narrator, PrisonOfficer)
        }
        cls.folder = next(i for i in cls.schedule if i.paths == ray.paths)
        cls.state = Presenter.new_state(cls.folder)
        cls.handler = MockHandler(cls.folder, cls.ensemble)

    @classmethod
    def branch_folder(cls, folder):
        if folder is not cls.folder:
            cls.state = Presenter.new_state(folder)
            cls.folder = folder

    @staticmethod
    def run_script(folder, script, references, handler, state):
        strict = folder in plotlines
        n = 0
        for n, (shot, item) in enumerate(run_through(
            script, references, strict=strict
        )):
            list(handler(shot, loop=None))
            list(handler(item, loop=None))
            print(item)
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
                self.handler, self.state
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
                self.handler, self.state
            )
            print(n)

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
        self.folder = folder

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
                self.handler, self.state
            )

        self.assertEqual(19780116, self.characters["Narrator"].get_state())
        self.assertEqual(
            Spot.w12_latimer_arches,
            self.characters["Narrator"].get_state(Spot)
        )

        folder = interlude(
            self.folder, index,
            self.ensemble, self.schedule,
            phrase=None
        )
        self.assertEqual(local.paths, folder.paths)
        self.folder = folder

