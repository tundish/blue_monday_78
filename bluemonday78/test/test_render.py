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

import bluemonday78.render


class RenderBaseTests(unittest.TestCase):

    def test_base_for_sanity(self):
        rv = bluemonday78.render.base_to_html()
        self.assertTrue(rv)
        self.assertFalse(rv[0].isspace())

    def test_base_cache(self):
        a = bluemonday78.render.base_to_html()
        b = bluemonday78.render.base_to_html()
        self.assertIs(a, b)

    def test_base_refresh(self):
        rv = bluemonday78.render.base_to_html()
        self.assertNotIn('http-equiv="refresh"' ,rv)
        rv = bluemonday78.render.base_to_html(refresh=12)
        self.assertIn('http-equiv="refresh"' ,rv)

    def test_base_body(self):
        rv = bluemonday78.render.base_to_html().format("<p>Body text</p>", "Error")
        self.assertIn("Body text",rv)
        self.assertNotIn("Error" ,rv)
