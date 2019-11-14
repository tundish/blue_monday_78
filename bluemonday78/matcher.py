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

from turberfield.dialogue.directives import Entity
from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import SceneScript
from turberfield.utils.misc import group_by_type

# TODO: Add matching over defined game timeframe

class MultiMatcher(Matcher):

    @staticmethod
    def parse_timespan(text):
        formats = {
            8: ("%Y%m%d", datetime.timedelta(days=1)),
            10: ("%Y%m%d%H", datetime.timedelta(hours=1)),
            12: ("%Y%m%d%H%M", datetime.timedelta(minutes=1)),
            14: ("%Y%m%d%H%M%S", datetime.timedelta(seconds=1)),
        }
        try:
            format_string, span = formats[len(text)]
        except KeyError:
            return text, ""
        else:
            return datetime.datetime.strptime(text, format_string), span

    @staticmethod
    def entity_states(folder):
        for script in SceneScript.scripts(**folder._asdict()):
            with script as dialogue:
                entities = group_by_type(dialogue.doc)[Entity.Declaration]
                for entity in entities:
                    yield from entity["options"].get("states", [])

    @staticmethod
    def decorate_folder(folder, min_t, max_t):
        for entity_state in (
            i for i in MultiMatcher.entity_states(folder) if i.isdigit()
        ):
            t, span = MultiMatcher.parse_timespan(entity_state)
            min_t = min(min_t, t) if min_t is not None else t
            max_t = max(max_t, t + span) if max_t is not None else t + span
        folder.metadata["min_t"] = min_t
        folder.metadata["max_t"] = max_t
        return folder

    def options(self, data):
        arc = data.get("arc", None)
        pathways = data.get("pathways", set())
        yield from (
            i for i in self.folders
            if arc is not None and i.metadata.get("arc") == arc
            or i.metadata.get("pathways", set()).intersection(pathways)
        )
