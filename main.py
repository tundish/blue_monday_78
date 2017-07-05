#!/usr/bin/env python
#   -*- encoding: UTF-8 -*-

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
import sys
import textwrap

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from turberfield.dialogue.handlers import TerminalHandler
from turberfield.dialogue.player import rehearse
from turberfield.utils.misc import log_setup

import logic

"""
Python 3.6 requires PyInstaller-3.3.dev0+gabfc806

"""

class GUIHandler(TerminalHandler):

    @staticmethod
    def display(widget, text):
        widget.configure(state="normal")
        widget.insert(tk.END, text)
        widget.insert(tk.END, "\n")
        widget.configure(state="disabled")
        widget.see(tk.END)

    @staticmethod
    def parse_command(cmd):
        try:
            return cmd.strip().split(" ")[-1][0].lower()
        except:
            return None

    def __init__(self, widget, *args, **kwargs):
        self.widget = widget
        self.buf = collections.deque()
        self.waiting = False
        super().__init__(None, *args, **kwargs)

    def handle_scenescript(self, obj):
        return 1

    def handle_scene(self, obj):
        self.display(self.widget, obj.scene.capitalize())
        return self.pause

    def handle_shot(self, obj):
        self.display(self.widget, obj.name.capitalize())
        return self.pause

    def handle_line(self, obj):
        if obj.persona is None:
            return 0

        name = getattr(obj.persona, "_name", "")
        self.display(self.widget, textwrap.indent(name, " " * 2))
        self.display(self.widget, textwrap.indent(obj.text, " " * 10))
        return self.pause + self.dwell * obj.text.count(" ")

    def handle_interlude(self, obj, folder, *args, **kwargs):
        if not self.buf:
            self.waiting = True
            interval = 5000
            self.display(self.widget, "Enter a command: ")
            self.widget.master.after(interval, self.handle_interlude, obj, folder, *args)
            return folder
        else:
            self.waiting = False
            cmd = "\n".join(self.buf)
            self.log.info(cmd)
            self.buf.clear()
            self.log.debug(args)
            return super().handle_interlude(*args, cmd=cmd, log=self.log, **kwargs)

class Presenter:

    def __init__(self, args, textarea):
        self.args = args
        self.textarea = textarea
        self.log = logging.getLogger("bluemonday")
        self.events = None
        self.handler = None

    def run(self):
        secs = 6
        root = self.textarea.master
        if not self.handler:
            self.handler = GUIHandler(
                self.textarea,
                dbPath=self.args.db,
                pause=self.args.pause,
                dwell=self.args.dwell,
                log=self.log
            )
            self.events = rehearse(
                logic.ray,
                logic.references,
                self.handler,
                strict=True
            )
            root.after(1, self.run)
        elif not self.handler.waiting:
            secs = next(self.events) or 6
        else:
            secs = 6

        root.after(int(secs * 1000), self.run)

    def on_enter(self, event):
        self.log.debug(event)
        widget = event.widget
        try:
            self.handler.buf.append(widget.get().strip())
        finally:
            widget.delete(0, tk.END)

def main(args):
    log = logging.getLogger(log_setup(args, "bluemonday"))

    n = 0
    root = tk.Tk()
    root.title("Blue Monday '78")
    root.geometry("500x400")

    entry = tk.Entry()
    entry.pack(side=tk.BOTTOM, fill=tk.X)
    text = ScrolledText(root)
    text.focus_set()
    text.pack(side=tk.LEFT, fill=tk.Y)

    if not n:
        text.configure(state="normal")
        text.insert(tk.END, "Enter a number: ")
        text.configure(state="disabled")
        entry.focus_set()

    p = Presenter(args, text)
    root.after(1, p.run)
    entry.bind("<Return>", p.on_enter)

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
        "--dwell", type=float, default=TerminalHandler.dwell,
        help="Time in seconds [{th.dwell}] to dwell on each word.".format(th=TerminalHandler)
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
