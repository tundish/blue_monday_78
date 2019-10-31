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

from collections import namedtuple

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
from turberfield.utils.misc import group_by_type


class Presenter:

    Animation = namedtuple("Animation", ["delay", "duration", "element"])

    @staticmethod
    def animate_lines(seq, dwell, pause):
        """ Generate animations for lines of dialogue."""
        offset = 0
        for line in seq:
            duration = pause + dwell * line.text.count(" ")
            yield Presenter.Animation(offset, duration, line)
            offset += duration

    @staticmethod
    def animate_stills(seq):
        """ Generate animations for still images."""
        yield from (
            Presenter.Animation(still.offset / 1000, still.duration / 1000, still)
            for still in seq
        )

    @staticmethod
    def dialogue(folders, ensemble, strict=True, roles=1):
        """ Return the next selected scene script as compiled dialogue."""
        for folder in folders:
            for script in SceneScript.scripts(**folder._asdict()):
                with script as dialogue:
                    selection = dialogue.select(ensemble, roles=roles)
                    if selection and all(selection.values()):
                        return dialogue.cast(selection).run()
                    elif not strict and any(selection.values()):
                        return dialogue.cast(selection).run()

    def __init__(self, dialogue):
        self.frames = [group_by_type(i.items) for i in dialogue.shots]

    @property
    def pending(self) -> int:
        return len([
            frame for frame in self.frames
            if all([Performer.allows(i) for i in frame[Model.Condition]])
        ])

    def frame(self, dwell=0.3, pause=1, react=True):
        """ Return the next shot of dialogue as an animated frame."""
        while True:
            frame = self.frames.pop(0)
            if all([Performer.allows(i) for i in frame[Model.Condition]]):
                frame[Model.Line] = list(
                    self.animate_lines(frame[Model.Line], dwell, pause)
                )
                frame[Model.Still] = list(self.animate_stills(frame[Model.Still]))
                for p in frame[Model.Property]:
                    if react and p.object is not None:
                        setattr(p.object, p.attr, p.val)
                return frame
