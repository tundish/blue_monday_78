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
from turberfield.utils.misc import group_by_type

from bluemonday78.logic import ensemble, plotlines, schedule


class Player:

    @staticmethod
    def next(folders, ensemble, strict=True, roles=1):
        for folder in folders:
            scripts = SceneScript.scripts(**folder._asdict())
            for script in scripts:
                with script as dialogue:
                    selection = dialogue.select(ensemble, roles=roles)
                    if all(selection.values()):
                        return (script, selection)
                    elif not strict and any(selection.values()):
                        return (script, selection)
        else:
            return None

    @property
    def stopped(self):
        return not bool(self.next(self.folders, self.ensemble))

    def init(self, folders, ensemble):
        self.folders = folders
        self.ensemble = ensemble

    def __init__(self, folders, ensemble):
        self.shots = []
        self.init(folders, ensemble)

    def react(self, obj):
        if isinstance(obj, Model.Property):
            if obj.object is not None:
                setattr(obj.object, obj.attr, obj.val)
        return obj

    def run(self, handler=None):
        handler = handler or self.react
        try:
            script, selection = self.next(self.folders, self.ensemble)
        except TypeError:
            raise GeneratorExit
        with script as dialogue:
            model = dialogue.cast(selection).run()
            for shot, item in model:
                yield handler(shot)
                yield handler(item)
                if not self.shots or self.shots[-1].name != shot.name:
                        self.shots.append(shot._replace(items=None))

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.ensemble = ensemble()
        self.schedule = copy.deepcopy(schedule)
        self.characters = {
            k.__name__: v for k, v in group_by_type(self.ensemble).items()
        }

    def test_stopped(self):
        player = Player(self.schedule, self.ensemble)
        self.assertFalse(player.stopped)

    def test_play(self):
        player = Player(self.schedule, self.ensemble)
        self.assertEqual(148, len(list(player.run())))
        self.assertEqual(6, len(player.shots))
        self.assertEqual("ray does the paperwork", player.shots[-1].name)

    def test_run(self):
        player = Player(self.schedule, self.ensemble)
        while True:
            list(player.run())
            print(*player.shots, sep="\n")
            print()
