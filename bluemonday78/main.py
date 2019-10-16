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

import argparse
import collections
import logging
from numbers import Number
import sys
import textwrap

import tkinter as tk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText

from turberfield.dialogue.handlers import TerminalHandler
from turberfield.dialogue.performer import Performer
from turberfield.utils.misc import log_setup

from bluemonday78 import logic
from bluemonday78 import __version__


DEFAULT_PAUSE = 1.2
DEFAULT_DWELL = 0.3


class GUIHandler(TerminalHandler):

    @staticmethod
    def register_fonts(widget):
        fonts = {
            "direction": Font(family="Helvetica", size=12),
            "titles": Font(family="Helvetica", size=12, weight="bold"),
            "narrator": Font(family="Courier", size=12, slant="italic"),
            "speaker": Font(family="Courier", size=12, weight="normal"),
            "speech": Font(family="Courier", size=12, weight="bold"),
        }
        for k, v in fonts.items():
            widget.tag_config(k, font=v)
        return fonts

    @staticmethod
    def display(widget, text="", tags=()):
        widget.configure(state="normal")
        if not tags:
            widget.insert(tk.END, text)
        else:
            widget.insert(tk.END, text, tags)
        widget.insert(tk.END, "\n")
        widget.configure(state="disabled")
        widget.see(tk.END)

    @staticmethod
    def announce(speaker):
        if isinstance(speaker, logic.Player):
            return "{0.firstname} {0.surname}".format(speaker.name)
        else:
            try:
                return speaker.name.firstname
            except AttributeError:
                return ""

    @staticmethod
    def parse_command(cmd):
        try:
            return cmd.strip().split(" ")[-1][0].lower()
        except Exception:
            return None

    def __init__(self, widget, references, *args, **kwargs):
        self.widget = widget
        self.references = references
        self.buf = collections.deque()
        self.speaker = None
        try:
            super().__init__(None, *args, **kwargs)
        except UserWarning:
            # NOTE: dev on 12.04
            pass

    def handle_property(self, obj):
        if obj.object is not None:
            try:
                setattr(obj.object, obj.attr, obj.val)
                self.log.debug("Property {0}.{1} set to {2}.".format(
                    obj.object, obj.attr, obj.val
                ))
            except AttributeError as e:
                self.log.error(". ".join(getattr(e, "args", e) or e))
        return 0

    def handle_scenescript(self, obj):
        return 1

    def handle_scene(self, obj):
        self.display(self.widget, obj.scene.capitalize(), tags=("titles",))
        self.display(self.widget, tags=("titles",))
        self.speaker = None
        return self.pause

    def handle_shot(self, obj):
        self.display(self.widget)
        return self.pause

    def handle_line(self, obj):
        if obj.persona is None:
            return 0

        # TODO: Fix this properly in turberfield-dialogue
        text = obj.text.replace("   ", " ").replace("  ", " ")
        if self.speaker is not obj.persona:
            self.speaker = obj.persona
            self.display(
                self.widget,
                textwrap.indent(
                    self.announce(self.speaker),
                    " " * 2
                ),
                tags=("speaker",)
            )

        tags = ("narrator",) if isinstance(self.speaker, logic.Narrator) else ("speech",)

        self.display(
            self.widget,
            textwrap.indent(textwrap.fill(text, width=60), " " * 10),
            tags=tags
        )
        self.display(self.widget)
        return self.pause + self.dwell * text.count(" ")


class Presenter:

    titles = [(
        textwrap.dedent(
            """
                Blue Monday '78.
            """
        ), "titles"),
        ("    Version {version}".format(version=__version__), "direction"),
        (textwrap.dedent(
            """
            An interactive dialogue test piece.
            Written during the Summer Novel Festival 2017 Game Jam.
            """
        ).format(version=__version__), "titles"),
        (
        "    All characters are fictional.\n"
        "    Contains strong language.", "direction"),
        (textwrap.dedent("""
        First, pick a name for the main character.
        Type it as 'title firstname surname', eg:
        """), "titles"),
        ("    Mr Maurice Micklewhite", "narrator"),
    ]

    credits = textwrap.indent(textwrap.dedent(
        """

        Programming:

                  tundish

        Soundtrack:

            JunkDLC featuring P'role

        Written and produced by:

                 D Haynes



                 © MMXVII

        """), " " * 16)

    def __init__(self, args, textarea, entry):
        self.args = args
        self.textarea = textarea
        self.entry = entry
        self.log = logging.getLogger("bluemonday")
        self.handler = None
        self.player = None
        self.buf = collections.deque()
        self.seq = collections.deque()
        self.ensemble = list(logic.associations().ensemble())
        self.folder = logic.ray
        self.state = None
        self.interlude = None
        self.prompt = None
        self.entry.bind("<Return>", self.on_input)
        self.performer = Performer(logic.schedule, self.ensemble)

        root = self.textarea.master
        root.after(200, self.play)

    @staticmethod
    def blocked(ensemble):
        hipster = next(i for i in ensemble if isinstance(i, logic.Narrator))
        return hipster.get_state() == 19780118

    @property
    def autoplay(self):
        return not self.blocked(self.ensemble)

    def play(self):
        secs = getattr(self.handler, "pause", 1)
        root = self.textarea.master
        if self.seq:
            item = self.seq.popleft()
            rv = list(self.handler(item, loop=root))
            secs = rv[0] if rv and isinstance(rv[0], Number) else secs
            self.log.debug(secs)
        elif self.performer.stopped:
            self.handler.display(self.textarea, self.credits, tags=("titles",))
            return
        elif self.player and self.handler and self.prompt is None:
            self.prompt = "Press return."
            self.handler.display(self.textarea, self.prompt)
        root.after(int(secs * 1000), self.play)

    def run(self, reload=False):
        root = self.textarea.master
        if not self.handler:
            self.handler = GUIHandler(
                self.textarea,
                logic.references,
                dbPath=self.args.db,
                pause=self.args.pause,
                dwell=self.args.dwell,
                log=self.log
            )
            try:
                list(self.handler(logic.references, loop=root))
            except AttributeError:
                # NOTE: dev on 12.04
                pass
            root.after(1, self.run)
            return
        elif not self.seq:
            self.seq.extend(list(self.performer.run(react=False)))

    def on_input(self, event):
        widget = event.widget
        try:
            val = widget.get().strip()
            self.buf.append(val)
            GUIHandler.display(self.textarea, val, ("narrator",))
            GUIHandler.display(self.textarea)
            if not self.player:
                self.player = logic.Player(name=val).set_state(logic.Spot.w12_ducane_prison)
                try:
                    player = next(i for i in self.ensemble if isinstance(i, logic.Player))
                    self.ensemble.remove(player)
                except (StopIteration, ValueError) as e:
                    self.log.debug(e)
                finally:
                    self.ensemble.append(self.player)
                    self.log.debug(self.player)
                self.buf.clear()
                widget.master.after(1, self.run)
            elif self.prompt:
                cmd = "\n".join(self.buf)
                self.log.debug(cmd)
                self.buf.clear()
                self.prompt = None
                widget.master.after(200, self.run)
        finally:
            widget.delete(0, tk.END)


def main(args):
    log = logging.getLogger(log_setup(args, "bluemonday"))

    root = tk.Tk()
    root.title("Blue Monday '78")

    entry = tk.Entry()
    entry.pack(side=tk.BOTTOM, fill=tk.X)

    widget = ScrolledText(root)
    width = GUIHandler.register_fonts(widget)["speech"].measure("0" * 76)
    widget.focus_set()
    widget.pack(fill=tk.BOTH, expand=True)

    root.geometry("{0}x400".format(int(width)))
    log.debug("{0} wide.".format(width))

    for text, tag in Presenter.titles:
        GUIHandler.display(widget, text, tags=(tag,))
    GUIHandler.display(widget)
    GUIHandler.display(widget, "Enter your player name: ", tags=("direction",))

    Presenter(args, widget, entry)
    tk.mainloop()


def parser(description=__doc__):
    rv = argparse.ArgumentParser(
        description,
        fromfile_prefix_chars="@"
    )
    rv.add_argument(
        "--version", action="store_true", default=False,
        help="Print the current version number")
    rv.add_argument(
        "-v", "--verbose", required=False,
        action="store_const", dest="log_level",
        const=logging.DEBUG, default=logging.INFO,
        help="Increase the verbosity of output")
    rv.add_argument(
        "--log", default=None, dest="log_path",
        help="Set a file path for log output")
    rv.add_argument(
        "--pause", type=float, default=DEFAULT_PAUSE,
        help="Time in seconds [{0:0.3}] to pause after a line.".format(DEFAULT_PAUSE)
    )
    rv.add_argument(
        "--dwell", type=float, default=DEFAULT_DWELL,
        help="Time in seconds [{0:0.3}] to dwell on each word.".format(DEFAULT_DWELL)
    )
    rv.add_argument(
        "--db", required=False, default=None,
        help="Database URL.")
    rv.add_argument(
        "--session", required=False, default="",
        help="Session id (internal use only)")
    return rv


def run():
    p = parser()
    args = p.parse_args()

    rv = 0
    if args.version:
        sys.stdout.write(__version__)
        sys.stdout.write("\n")
    else:
        rv = main(args)

    if rv == 2:
        sys.stderr.write("\n Missing command.\n\n")
        p.print_help()

    sys.exit(rv)


if __name__ == "__main__":
    run()
