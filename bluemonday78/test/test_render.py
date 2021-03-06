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

import unittest

from bluemonday78.presenter import Presenter
import bluemonday78.render
from bluemonday78.test.test_presenter import DialogueLoader
import bluemonday78.story
from bluemonday78.types import Character
from bluemonday78.types import Location
from bluemonday78.types import Spot


class RenderBaseTests(unittest.TestCase):

    def test_base_for_sanity(self):
        rv = bluemonday78.render.body_html()
        self.assertTrue(rv)
        self.assertFalse(rv[0].isspace())

    def test_base_cache(self):
        a = bluemonday78.render.body_html()
        b = bluemonday78.render.body_html()
        self.assertIs(a, b)

    def test_base_refresh(self):
        rv = bluemonday78.render.body_html()
        self.assertNotIn('http-equiv="refresh"' ,rv)
        rv = bluemonday78.render.body_html(refresh=12)
        self.assertIn('http-equiv="refresh"' ,rv)

    def test_base_body(self):
        rv = bluemonday78.render.body_html().format(
            "",
            "<p>Body text</p>",
            "Error"
        )
        self.assertIn("Body text",rv)
        self.assertNotIn("Error" ,rv)


class RenderFrameTests(DialogueLoader, unittest.TestCase):

    def test_prologue_frame(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        frame = presenter.frame()
        rv = bluemonday78.render.frame_to_html(frame)
        self.assertEqual(1, rv.count('<blockquote class="obj-line">'), rv)
        self.assertEqual(3, rv.count("<img "))

    def test_epilogue_frame(self):
        dialogue = self.presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        while presenter.pending:
            frame = presenter.frame()
        rv = bluemonday78.render.frame_to_html(frame)
        self.assertEqual(1, rv.count("<audio"))

    def test_map_from_ensemble_empty(self):
        ensemble = [Location(label=i.name).set_state(i) for i in Spot]
        ensemble.append(bluemonday78.story.build_narrator())
        rv = bluemonday78.render.ensemble_to_html(ensemble)
        self.assertEqual(0, rv.count("<form"), rv)

    def test_map_from_ensemble(self):
        totals = list(range(len(Spot)))
        self.assertTrue(totals)
        for index in totals:
            ensemble = [Location(label=i.name).set_state(i) for i in Spot]
            with self.subTest(index=index):
                for locn in ensemble[:index]:
                    ensemble.append(
                        Character(name="A").set_state(locn.get_state(Spot))
                    )
                ensemble.append(bluemonday78.story.build_narrator())
                rv = bluemonday78.render.ensemble_to_html(ensemble)
                self.assertEqual(index, rv.count("<form"), rv)


class RenderStyleTests(DialogueLoader, unittest.TestCase):

    def test_blank(self):
        rv = bluemonday78.render.dict_to_css()
        self.assertEqual(":root {\n\n}", rv)

    def test_strings(self):
        rv = bluemonday78.render.dict_to_css(dict(apple="monospace"))
        self.assertEqual(":root {--apple: monospace;}", rv.replace("\n", ""))

    def test_numbers(self):
        data = {"color-hue": 35}
        rv = bluemonday78.render.dict_to_css(data)
        self.assertEqual(":root {--color-hue: 35;}", rv.replace("\n", ""))

    def test_compund(self):
        data = {
            "yellow-hue": 50,
            "creamy": "hsl(var(--yellow-hue), 0%, 100%, 1.0)",
        }
        rv = bluemonday78.render.dict_to_css(data)
        self.assertEqual(
            ":root {--yellow-hue: 50;--creamy: hsl(var(--yellow-hue), 0%, 100%, 1.0);}",
            rv.replace("\n", "")
        )
