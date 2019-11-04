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
import pathlib
import sys
import uuid

__doc__ = """
Generate Python code to describe SceneScript folders from a directory
structure.

"""

def find_locations(path):
    for id_location in path.glob("**/uuid.hex"):
        try:
            uid = uuid.UUID(hex=id_location.read_text().strip())
        except (ValueError, OSError):
            print("Bad uuid at '", id_location, "'.", sep="", file=sys.stderr)
            continue
        else:
            yield uid

def main(args):
    for path in args.paths:
        print(*list(find_locations(path)), sep="\n")
    return 0

def parser(description=__doc__):
    rv = argparse.ArgumentParser(
        description,
        fromfile_prefix_chars="@"
    )
    rv.add_argument(
        "paths", nargs="*", type=pathlib.Path,
        help="supply a list of directory paths"
    )
    return rv


if __name__ == "__main__":
    p = parser()
    args = p.parse_args()
    rv = main(args)
    sys.exit(rv)
