#!/usr/bin/env python3
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

import itertools
import unittest

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript

from bluemonday78.presenter import Presenter
import bluemonday78.story
from bluemonday78.types import Character
from bluemonday78.types import Narrator


class DialogueLoader:

    def setUp(self):
        self.folders = [
            SceneScript.Folder(
                pkg="bluemonday78",
                description="A Spike for Folder patterns.",
                metadata={"location": "inner"},
                paths=[
                    "dialogue/outer/inner/story/scene_01.rst",
                ],
                interludes=itertools.repeat(None)
            )
        ]
        self.ensemble = [
            Character(name="A Test Actor").set_state(10),
            bluemonday78.story.build_narrator()

        ]
        self.presenter = Presenter(None, self.ensemble)


class PresenterTests(DialogueLoader, unittest.TestCase):

    def test_frame(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        shot_index = 0
        self.assertEqual(10, self.ensemble[0].state)
        while presenter.pending:
            with self.subTest(shot_index=shot_index):
                frame = presenter.frame()
                self.assertTrue(frame)
                shot_index += 1
        self.assertEqual(3, shot_index)
        self.assertEqual(20, self.ensemble[0].state)

    def test_prologue(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        frame = presenter.frame()
        self.assertEqual(3, len(frame[Model.Still]))
        self.assertEqual(0, len(frame[Model.Audio]))
        self.assertTrue(
            all(isinstance(i, Presenter.Animation) for i in frame[Model.Still])
        )
        self.assertTrue(
            all(isinstance(i.element, Model.Still) for i in frame[Model.Still])
        )
        self.assertEqual(20, max(i.duration for i in frame[Model.Still]))
        self.assertEqual(20000, max(i.element.duration for i in frame[Model.Still]))
        self.assertEqual(1, len(frame[Model.Line]))
        self.assertTrue(
            all(isinstance(i, Presenter.Animation) for i in frame[Model.Line])
        )
        self.assertTrue(
            all(isinstance(i.element, Model.Line) for i in frame[Model.Line])
        )

    def test_option_0(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        while presenter.pending != 1:
            frame = presenter.frame()
        self.assertEqual(0, len(frame[Model.Still]))
        self.assertEqual(1, len(frame[Model.Line]))
        self.assertEqual(0, len(frame[Model.Audio]))
        self.assertTrue(
            all(isinstance(i, Presenter.Animation) for i in frame[Model.Line])
        )
        self.assertTrue(
            all(isinstance(i.element, Model.Line) for i in frame[Model.Line])
        )
        self.assertEqual("On.", frame[Model.Line][0].element.text)

    def test_epilogue(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        while presenter.pending:
            frame = presenter.frame()
        self.assertEqual(0, len(frame[Model.Still]))
        self.assertEqual(1, len(frame[Model.Line]))
        self.assertEqual(1, len(frame[Model.Audio]))
        self.assertTrue(
            all(isinstance(i, Presenter.Animation) for i in frame[Model.Line])
        )
        self.assertTrue(
            all(isinstance(i.element, Model.Line) for i in frame[Model.Line])
        )
        self.assertEqual(
            "Goodbye from  Actor .",
            frame[Model.Line][0].element.text
        )


class ValidationTests(unittest.TestCase):

    def test_allowed(self):
        for text in (
            "http://foo.com/blah_blah",
            "http://foo.com/blah_blah/",
            "http://www.example.com/wpstyle/?p=364",
            "http://142.42.1.1/",
            "http://142.42.1.1:8080/",
        ):
            with self.subTest(text=text):
                self.assertTrue(Presenter.validation["url"].match(text))

    def test_blocked(self):
        for text in (
            "http://.www.foo.bar/",
            "h://test",
        ):
            with self.subTest(text=text):
                self.assertFalse(Presenter.validation["url"].match(text))
