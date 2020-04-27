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
import mimetypes
import pathlib
import sys

def main(args):
    for path in args.paths:
        if path.is_file():
            print(path, mimetypes.guess_type(path))
        else:
            print(path)

def parser(description=__doc__):
    rv = argparse.ArgumentParser(
        description,
        fromfile_prefix_chars="@"
    )
    rv.add_argument(
        "paths", nargs="*", type=pathlib.Path,
        help="supply a list of file paths"
    )
    return rv


if __name__ == "__main__":
    p = parser()
    args = p.parse_args()
    rv = main(args)
    sys.exit(rv)

