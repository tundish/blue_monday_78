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
from collections import defaultdict
from collections import namedtuple
import glob
import os.path
import pathlib
import platform
import pprint
import sys
import uuid

__doc__ = """
Identify assets related to SceneScript folders.

NB: In order to reference a story arc from a different pathway, do `ln -s`, eg::

    ln -rs -t bluemonday78/dialogue/w12_ducane/prison_wing \
    bluemonday78/dialogue/w12_ducane/prison_office/release

This creates a relative soft link in `prison_wing` which will point to
`prison_office/release`.

"""

Assets = namedtuple("Assets", ["id", "pathways", "arc", "scripts"])


def find_scripts(path):
    for id_location in glob.glob(os.path.join(path, "**/uuid.hex"), recursive=True):
        try:
            id_path = pathlib.Path(id_location)
            uid = uuid.UUID(hex=id_path.read_text().strip())
        except (ValueError, OSError):
            print("Bad uuid at '", id_path, "'.", sep="", file=sys.stderr)
            continue
        else:
            for script_path in sorted(id_path.parent.glob("*.rst")):
                yield uid, script_path


def find_assets(path, prefix=""):
    locations = defaultdict(list)
    for uid, script_path in find_scripts(path):
        locations[uid].append(script_path)

    for uid, script_paths in locations.items():
        arc_name = None
        pathways = set()
        scripts = set()
        for script_path in script_paths:
            arc_path = script_path.parent
            pathways.add(arc_path.parent.relative_to(path).parts)
            if not arc_path.is_symlink():
                arc_name = arc_path.name
                arc_name = ".".join((
                    prefix, str(arc_path.relative_to(path)).replace(os.sep, ".")
                ))
                scripts.add(script_path.relative_to(path))

        if "windows" in platform.system().lower():
            # Find soft links explicitly because MS OS fails to do it
            # within the source repository
            links = set([
                (pathlib.Path(f).parent, pathlib.Path(f).read_text())
                for script in script_paths
                for f in glob.glob(os.path.join(
                    path, "{0}/{1}".format("**", script.parent.name)),
                    recursive=True)
                if pathlib.Path(f).is_file() and
                0 < pathlib.Path(f).stat().st_size < 128
            ])
            for parent, hop in links:
                if parent.joinpath(hop).resolve() == arc_path.resolve():
                    pathways.add(parent.relative_to(path).parts)

        yield Assets(
            uid, frozenset(pathways),
            arc_name, tuple(sorted(scripts))
        )


def main(args):
    assets = [i for path in args.paths for i in find_assets(path)]
    pprint.pprint(assets)


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
