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

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.player import rehearse

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
from bluemonday78.logic import ray
from bluemonday78.logic import Spot
from bluemonday78.logic import ensemble
from bluemonday78.logic import schedule
from bluemonday78.main import GUIHandler
from bluemonday78.main import Presenter


class MockHandler(GUIHandler):

    def __init__(self, parent, folder, references):
        self.parent = parent
        self.folder = folder
        self.references = references
        self.calls = 0
        self.visits = Counter()
        super().__init__(widget=None)

    def __call__(self, obj, *args, **kwargs):
        rv = obj
        if isinstance(obj, Callable):
            folder, index, ensemble, branches = args
            rv = obj(
                folder, index, self.references,
                branches=branches,
                phrase=None
            )
        yield rv


class SceneTests(unittest.TestCase):

    def setUp(self):
        self.schedule = copy.deepcopy(schedule)
        self.ensemble = ensemble()

    def test_interlude(self):
        hipster = next(i for i in self.ensemble if isinstance(i, Hipster))
        player = next(i for i in self.ensemble if isinstance(i, Player))
        narrator = next(i for i in self.ensemble if isinstance(i, Narrator))

        folder = copy.deepcopy(schedule)
        test_handler = MockHandler(self, folder, self.ensemble)
        self.assertTrue(next(MatchMaker.match("OK"), None))
        self.assertFalse(next(MatchMaker.match("frankie"), None))
        rv = list(rehearse(
            folder, self.ensemble, test_handler,
            branches=schedule,
            repeat=0, strict=True, roles=1,
            loop=None
        ))
