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

from turberfield.utils.misc import group_by_type

from bluemonday78.logic import ensemble, plotlines, schedule
from bluemonday78.performer import Performer


class TestPerformer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.ensemble = ensemble()
        self.schedule = copy.deepcopy(schedule)
        self.characters = {
            k.__name__: v for k, v in group_by_type(self.ensemble).items()
        }

    def test_stopped(self):
        performer = Performer(self.schedule, self.ensemble)
        self.assertFalse(performer.stopped)

    def test_play(self):
        performer = Performer(self.schedule, self.ensemble)
        self.assertEqual(150, len(list(performer.run())))
        self.assertEqual(6, len(performer.shots))
        self.assertEqual("ray does the paperwork", performer.shots[-1].name)

    def test_run(self):
        performer = Performer(self.schedule, self.ensemble)
        while not performer.stopped:
            list(performer.run())
