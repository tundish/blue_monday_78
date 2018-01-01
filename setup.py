#!/usr/bin/env python
# encoding: UTF-8

import ast
from setuptools import setup
import os.path

__doc__ = open(
    os.path.join(os.path.dirname(__file__), "README.rst"),
    "r"
).read()

try:
    # For setup.py install
    from bluemonday_78 import __version__ as version
except ImportError:
    # For pip installations
    version = str(ast.literal_eval(
        open(os.path.join(
            os.path.dirname(__file__),
            "bluemonday78",
            "__init__.py"),
            "r"
        ).read().split("=")[-1].strip()
    ))

setup(
    name="bluemonday78",
    version=version,
    description="A dramatic screenplay",
    author="D Haynes",
    author_email="tundish@gigeconomy.org.uk",
    url="https://github.com/tundish/blue_monday_78",
    long_description=__doc__,
    classifiers=[
        "Framework :: Turberfield",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3"
        " or later (AGPLv3+)"
    ],
    packages=["bluemonday78", "bluemonday78.test"],
    package_data={
        "bluemonday78": [
            "justin_19780116_fired/*",
            "ray_19780116_retires/*",
            "w12_19780116_local/*",
        ]
    },
    install_requires=[
        "turberfield-dialogue>=0.13.0[audio]",
        "turberfield-utils>=0.33.0",
    ],
    zip_safe=True,
    entry_points={}
)
