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

import argparse
import collections
import itertools
import logging
import sys
import textwrap

import tkinter as tk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText

from turberfield.dialogue.handlers import TerminalHandler
from turberfield.dialogue.player import run_through
from turberfield.dialogue.model import SceneScript
from turberfield.utils.misc import log_setup

from bluemonday78 import logic


DEFAULT_DWELL = TerminalHandler.dwell + 0.1


class GUIHandler(TerminalHandler):

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
        except:
            return None

    def __init__(self, widget, *args, **kwargs):
        self.widget = widget
        self.buf = collections.deque()
        self.speaker = None
        self.widget.tag_config("speaker", font=Font(family="Courier", size=12, weight="normal"))
        self.widget.tag_config("speech", font=Font(family="Courier", size=12, weight="bold"))
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
        self.display(self.widget, obj.scene.capitalize())
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

        self.display(
            self.widget,
            textwrap.indent(textwrap.fill(text, width=60), " " * 10),
            tags=("speech",)
        )
        self.display(self.widget)
        return self.pause + self.dwell * text.count(" ")

class Presenter:

    def __init__(self, args, textarea, entry):
        self.args = args
        self.textarea = textarea
        self.entry = entry
        self.log = logging.getLogger("bluemonday")
        self.events = None
        self.handler = None
        self.player = None
        self.buf = collections.deque()
        self.seq = collections.deque()
        self.folder = logic.ray
        self.state = None
        self.phrase = None
        self.interlude = None
        self.prompt = None
        self.entry.bind("<Return>", self.on_input)

        root = self.textarea.master
        root.after(200, self.play)

    def play(self):
        secs = getattr(self.handler, "pause", 1)
        root = self.textarea.master
        if self.seq:
            item = self.seq.popleft()
            rv = list(self.handler(item, loop=root))
            secs = rv[0] if rv and isinstance(rv[0], int) else secs
        elif self.handler and self.prompt is None:
            self.prompt = " ".join(sorted(logic.MatchMaker.words()))
            self.handler.display(self.textarea, self.prompt)
        root.after(int(secs * 1000), self.play)

    def new_state(self, folder):
        return zip(
            itertools.count(),
            SceneScript.scripts(**folder._asdict()),
            folder.interludes
        )

    def run(self, reload=False):
        root = self.textarea.master
        if not self.handler:
            self.handler = GUIHandler(
                self.textarea,
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
            self.state = self.new_state(self.folder)
            root.after(1, self.run)
            return
        elif not self.seq:
            if self.interlude and self.phrase:
                # TODO: create Line and send it to the handler
                self.handler.display(self.textarea, self.phrase.gist)
                folder = self.interlude(
                    self.folder, self.index,
                    logic.references, logic.schedule,
                    phrase=self.phrase
                )
                self.phrase = None
                self.prompt = None
                if folder is not self.folder:
                    self.state = self.new_state(folder)
                    self.folder = folder

            n = 0
            while not n:
                try:
                    self.index, script, self.interlude = next(self.state)
                    self.seq.append(script)
                    strict = self.folder in logic.plotlines
                    self.log.info(self.folder.paths[self.index])
                    self.log.info("Strict mode on." if strict else "Strict mode off.")
                    for shot, item in run_through(script, logic.references, strict=strict):
                        n += 1
                        self.seq.append(shot)
                        self.seq.append(item)
                    self.log.info("Read ahead {0}".format(n))
                except StopIteration:
                    # Wait for an input phrase
                    return

    def on_input(self, event):
        widget = event.widget
        try:
            val = widget.get().strip()
            self.buf.append(val)
            GUIHandler.display(self.textarea, val)
            if not self.player:
                self.player = logic.Player(name=val).set_state(logic.Spot.w12_ducane_prison)
                try:
                    player = next(i for i in logic.references if isinstance(i, logic.Player))
                    logic.references.remove(player)
                except (StopIteration, ValueError):
                    pass
                finally:
                    logic.references.append(self.player)
                self.log.debug(self.player)
                self.buf.clear()
                widget.master.after(1, self.run)
            elif not self.seq:
                cmd = "\n".join(self.buf)
                self.log.debug(cmd)
                self.phrase = next(logic.MatchMaker.match(cmd), None)
                self.log.debug(self.phrase)
                if self.phrase is not None:
                    self.buf.clear()
                widget.master.after(200, self.run)
        finally:
            widget.delete(0, tk.END)


def main(args):
    log = logging.getLogger(log_setup(args, "bluemonday"))

    n = 0
    root = tk.Tk()
    root.title("Blue Monday '78")
    root.geometry("560x400")

    entry = tk.Entry()
    entry.pack(side=tk.BOTTOM, fill=tk.X)
    text = ScrolledText(root)
    text.focus_set()
    text.pack(side=tk.LEFT, fill=tk.Y)

    GUIHandler.display(text, "Enter your player name: ")

    p = Presenter(args, text, entry)
    tk.mainloop()

def parser(description=__doc__):
    rv =  argparse.ArgumentParser(
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
        "--pause", type=float, default=TerminalHandler.pause,
        help="Time in seconds [{th.pause}] to pause after a line.".format(th=TerminalHandler)
    )
    rv.add_argument(
        "--dwell", type=float, default=DEFAULT_DWELL,
        help="Time in seconds [{0}] to dwell on each word.".format(DEFAULT_DWELL)
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
