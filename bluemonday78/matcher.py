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

import datetime
import logging

from turberfield.dialogue.directives import Entity
from turberfield.dialogue.directives import Pathfinder
from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import SceneScript
from turberfield.utils.misc import group_by_type

from bluemonday78.types import Narrator
from bluemonday78.types import Spot


class MultiMatcher(Matcher):

    @staticmethod
    def entity_states(folder):
        for script in SceneScript.scripts(**folder._asdict()):
            with script as dialogue:
                entities = group_by_type(dialogue.doc)[Entity.Declaration]
                for entity in entities:
                    yield from entity["options"].get("states", [])

    @staticmethod
    def decorate_folder(folder, min_t, max_t):
        integer_states = [i for i in MultiMatcher.entity_states(folder) if i.isdigit()]
        object_states = [
            Pathfinder.string_import(i) for i in MultiMatcher.entity_states(folder) if i not in integer_states
        ]
        folder.metadata["spots"] = {i for i in object_states if isinstance(i, Spot)}
        for entity_state in integer_states:
            t, span = Narrator.parse_timespan(entity_state)
            if span is not None:
                min_t = min(min_t, t if span else min_t) if min_t is not None else t
                max_t = max(max_t, (t + span) if span else max_t) if max_t is not None else t + span
                folder.metadata["min_t"] = min_t
                folder.metadata["max_t"] = max_t
        return folder

    def options(self, arc=None, t=None, pathways=None):
        for f in self.folders:
            if arc and f.metadata.get("arc", "") == arc:
                yield f
                continue

            if pathways and f.metadata.get("pathways", set()).intersection(pathways):
                yield f
                continue

            min_t = f.metadata.get("min_t", t)
            max_t = f.metadata.get("max_t", t)
            try:
                if min_t <= t <= max_t:
                    yield f
            except TypeError:
                continue
