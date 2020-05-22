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

from collections import defaultdict
from collections import deque
from collections import namedtuple
import copy
from datetime import datetime
import itertools
import logging
import math
import re
import sys

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
import turberfield.utils

import bluemonday78


class Presenter:

    Animation = namedtuple("Animation", ["delay", "duration", "element"])

    validation = {
        "email": re.compile(
            "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]"
            "+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9]"
            "(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+"
            # http://www.w3.org/TR/html5/forms.html#valid-e-mail-address
        ),
        "url": re.compile("(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$"),
        "location": re.compile("[0-9a-f]{32}"),
        "name": re.compile("[A-Z a-z]{2,42}"),
        "session": re.compile("[0-9a-f]{32}"),
    }

    definitions = {
        "creamy": "hsl(50, 0%, 100%, 1.0)",
        "pebble": "hsl(13, 0%, 30%, 1.0)",
        "claret": "hsl(13, 80%, 55%, 1.0)",
        "banana": "hsl(50, 80%, 55%, 1.0)",
        "collie": "hsl(76, 80%, 35%, 1.0)",
        "titles": '"AA Paro", sans-serif',
        "detail": '"Inknut Antiqua", sans-serif',
        "system": ", ".join([
            "BlinkMacSystemFont", '"Segoe UI"', "Roboto", '"Helvetica Neue"',
            '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"',
            "Arial", "sans-serif"
        ]),
    }

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
    def refresh_animations(frame, min_val=8):
        rv = min_val
        for typ in (Model.Line, Model.Still, Model.Audio):
            try:
                last_anim = frame[typ][-1]
                rv = max(rv, math.ceil(last_anim.delay + last_anim.duration))
            except IndexError:
                continue
        return rv

    def __init__(self, dialogue, ensemble=None):
        self.frames = [
            defaultdict(list, dict(
                {k: list(v) for k, v in itertools.groupby(i.items, key=type)},
                name=i.name, scene=i.scene
            ))
            for i in getattr(dialogue, "shots", [])
        ]
        self.ensemble = ensemble
        self.log = logging.getLogger(str(getattr(ensemble[-1], "id", "")) if ensemble else "")
        self.ts = datetime.utcnow()

    @property
    def pending(self) -> int:
        return len([
            frame for frame in self.frames
            if all([Performer.allows(i) for i in frame[Model.Condition]])
        ])

    @property
    def assembly(self):
        ensemble = [copy.copy(i) for i in self.ensemble]
        for obj in ensemble:
            if hasattr(obj, "memories"):
                obj.memories = [
                    i._replace(
                        subject=getattr(i.subject, "id", None),
                        object=getattr(i.object, "id", None)
                    )
                    for i in obj.memories
                ]
        return {
            "tooling": {
                i.__name__: i.__version__
                for i in (
                    turberfield.utils, turberfield.dialogue, bluemonday78
                )
            },
            "history": {
                "incept": self.ts,
                "extract": datetime.utcnow(),
            },
            "ensemble": ensemble,
        }

    def dialogue(self, folders, ensemble, strict=True, roles=2):
        """ Return the next selected scene script as compiled dialogue."""
        for folder in folders:
            for script in SceneScript.scripts(**folder._asdict()):
                with script as dialogue:
                    try:
                        selection = dialogue.select(ensemble, roles=roles)
                    except Exception as e:
                        self.log.error("Unable to process {0.fP}".format(script))
                        self.log.exception(e)
                        continue

                    if selection and all(selection.values()):
                        self.log.debug("Selection made strictly")
                    elif not strict and any(selection.values()):
                        self.log.debug("Selection made")
                    else:
                        continue

                    try:
                        return dialogue.cast(selection).run()
                    except Exception as e:
                        self.log.error("Unable to run {0.fP}".format(script))
                        self.log.exception(e)
                        continue

    def frame(self, dwell=0.3, pause=1, react=True):
        """ Return the next shot of dialogue as an animated frame."""
        while True:
            try:
                frame = self.frames.pop(0)
            except IndexError:
                self.log.debug("No more frames.")
                raise

            if all([Performer.allows(i) for i in frame[Model.Condition]]):
                frame[Model.Line] = list(
                    self.animate_lines(frame[Model.Line], dwell, pause)
                )
                frame[Model.Still] = list(self.animate_stills(frame[Model.Still]))
                for p in frame[Model.Property]:
                    if react and p.object is not None:
                        setattr(p.object, p.attr, p.val)
                for m in frame[Model.Memory]:
                    if react and m.object is None:
                        m.subject.set_state(m.state)
                    try:
                        if m.subject.memories[-1].state != m.state:
                            m.subject.memories.append(m)
                    except AttributeError:
                        m.subject.memories = deque([m], maxlen=6)
                    except IndexError:
                        m.subject.memories.append(m)
                return frame
