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

import copy
import unittest

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.player import rehearse

from bluemonday78.logic import Hipster
from bluemonday78.logic import MatchMaker
from bluemonday78.logic import Narrator
from bluemonday78.logic import Player
from bluemonday78.logic import references
from bluemonday78.logic import schedule

class SceneTests(unittest.TestCase):

    def setUp(self):
        self.references = references
        self.game = [copy.deepcopy(i) for i in schedule]

    def test_locations(self):
        hipster = next(i for i in self.references if isinstance(i, Hipster))
        player = next(i for i in self.references if isinstance(i, Player))
        narrator = next(i for i in self.references if isinstance(i, Narrator))

        class MockHandler:

            def __init__(self, parent, folder, references):
                self.parent = parent
                self.folder = folder
                self.references = references
                self.calls = 0
                self.visits = Counter()

