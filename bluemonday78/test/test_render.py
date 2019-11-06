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
        rv = bluemonday78.render.body_html().format("<p>Body text</p>", "Error")
        self.assertIn("Body text",rv)
        self.assertNotIn("Error" ,rv)


class RenderFrameTests(DialogueLoader, unittest.TestCase):

    def test_prologue_frame(self):
        dialogue = Presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        frame = presenter.frame()
        rv = bluemonday78.render.frame_to_html(frame)
        self.assertEqual(1, rv.count('<blockquote class="line">'))
        self.assertEqual(3, rv.count("<img "))

    def test_epilogue_frame(self):
        dialogue = Presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        while presenter.pending:
            frame = presenter.frame()
        rv = bluemonday78.render.frame_to_html(frame)
        self.assertEqual(1, rv.count("<audio"))

    def test_map_from_ensemble(self):
        ensemble = [Location(label=i.name).set_state(i) for i in Spot]
        rv = bluemonday78.render.ensemble_to_html(ensemble)
        self.assertEqual(7, rv.count("<form"))
