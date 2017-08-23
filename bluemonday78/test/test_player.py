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

from turberfield.dialogue.model import SceneScript
from turberfield.utils.misc import group_by_type

from bluemonday78.logic import ensemble, plotlines, schedule


class Player:

    @staticmethod
    def stopped(folders, ensemble, strict=True, roles=1):
        for folder in folders:
            scripts = SceneScript.scripts(**folder._asdict())
            for script in scripts:
                with script as dialogue:
                    selection = dialogue.select(ensemble, roles=roles)
                    if all(selection.values()):
                        return False
                    elif not strict and any(selection.values()):
                        return False
        else:
            return True

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ensemble = ensemble()
        cls.schedule = copy.deepcopy(schedule)
        cls.characters = {
            k.__name__: v for k, v in group_by_type(cls.ensemble).items()
        }

    def test_stopped(self):
        self.assertFalse(Player.stopped(self.schedule, self.ensemble))
