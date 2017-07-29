#!/usr/bin/env python
# encoding: UTF-8

from setuptools import setup
import os.path

__doc__ = open(
    os.path.join(os.path.dirname(__file__), "README.rst"),
    "r"
).read()

setup(
    name="bluemonday78",
    version="0.1.0",
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
    package_dir={"bluemonday78": "bluemonday78"},
    include_package_data=True,
    install_requires=["turberfield-dialogue"],
    zip_safe=True,
    entry_points={}
)
