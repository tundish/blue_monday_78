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

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

"""
Python 3.6 requires PyInstaller-3.3.dev0+gabfc806

"""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

n = 0
root = tk.Tk()
root.title("My Demo")
root.geometry("500x400")

entry = tk.Entry()
entry.pack(side=tk.BOTTOM, fill=tk.X)
text = ScrolledText(root)
text.focus_set()
text.pack(side=tk.LEFT, fill=tk.Y)

def on_enter(event):
    widget = event.widget
    try:
        n = int(widget.get().strip())
    except ValueError:
        pass
    else:
        text.configure(state="normal")
        text.insert(tk.END, "\n")
        for i in range(n):
            text.insert(tk.END, "This is line {0}\n".format(i))
        text.configure(state="disabled")
        text.see(tk.END)
    finally:
        widget.delete(0, tk.END)

entry.bind("<Return>", on_enter)

if not n:
    text.configure(state="normal")
    text.insert(tk.END, "Enter a number: ")
    text.configure(state="disabled")
    entry.focus_set()

tk.mainloop()
