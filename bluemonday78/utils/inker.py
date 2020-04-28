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

from PIL import Image
from PIL import ImageDraw
from PIL import ImageStat


def ink_from_grey(img:Image, sample=8, angle=0, scale=1, prescale=1):
    """

    Lifted gratefully from:

        https://github.com/philgyford/python-halftone.git
    """
    img = img.rotate(angle, expand=1)
    size = img.size[0] * scale, img.size[1] * scale
    half_tone = Image.new("L", size)
    draw = ImageDraw.Draw(half_tone)

    # Cycle through one sample point at a time, drawing a circle for
    # each one:
    for x in range(0, img.size[0], sample):
        for y in range(0, img.size[1], sample):

            # Area we sample to get the level:
            box = img.crop((x, y, x + sample, y + sample))

            # The average level for that box (0-255):
            mean = ImageStat.Stat(box).mean[0]

            # The diameter of the circle to draw based on the mean (0-1):
            diameter = (mean / 255) ** 0.5

            # Size of the box we'll draw the circle in:
            box_size = sample * scale

            # Diameter of circle we'll draw:
            # If sample=10 and scale=1 then this is (0-10)
            draw_diameter = diameter * box_size

            # Position of top-left of box we'll draw the circle in:
            # x_pos, y_pos = (x * scale), (y * scale)
            box_x, box_y = (x * scale), (y * scale)

            # Positioned of top-left and bottom-right of circle:
            # A maximum-sized circle will have its edges at the edges
            # of the draw box.
            x1 = box_x + ((box_size - draw_diameter) / 2)
            y1 = box_y + ((box_size - draw_diameter) / 2)
            x2 = x1 + draw_diameter
            y2 = y1 + draw_diameter

            draw.ellipse([(x1, y1), (x2, y2)], fill=255)

    half_tone = half_tone.rotate(-angle, expand=1)
    width_half, height_half = half_tone.size

    # Top-left and bottom-right of the image to crop to:
    xx1 = (width_half - img.size[0] * scale) / 2
    yy1 = (height_half - img.size[1] * scale) / 2
    xx2 = xx1 + img.size[0] * scale
    yy2 = yy1 + img.size[1] * scale

    half_tone = half_tone.crop((xx1, yy1, xx2, yy2))

    if prescale != 1:
        # Scale it back down to antialias the image.
        w = (xx2 - xx1) / prescale
        h = (yy2 - yy1) / prescale
        half_tone = half_tone.resize((w, h), resample=Image.LANCZOS)

    return half_tone


def main(args):
    for path in args.paths:
        if path.is_file() and str(mimetypes.guess_type(path)[0]).startswith(
            "image"
        ):
            output_path = path.with_suffix(".png")
            if output_path.exists():
                print("Protecting ", output_path, file=sys.stderr)
                continue
            with Image.open(path) as img:
                print("Processing ", path, file=sys.stderr)
                greyscale = img.convert("L")
                half_tone = ink_from_grey(greyscale, sample=8, angle=38)
                output_path = path.with_suffix(".png")
                print("Saving ", output_path, file=sys.stderr)
                half_tone.save(output_path)


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

