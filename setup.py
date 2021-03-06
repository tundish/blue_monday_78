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
    packages=[
        "bluemonday78",
        "bluemonday78.test",
        "bluemonday.utils"
    ],
    package_data={
        "bluemonday78": [
            "*.cfg",
            "dialogue/*/*/*/*.rst",
            #"static/audio/*.mp3",
            "static/css/*.css",
            "static/fonts/*.otf",
            "static/fonts/*.woff",
            "static/fonts/*.woff2",
            "static/img/*/*.jpg",
        ]
    },
    install_requires=[
        "aiohttp>=3.6.2",
        "turberfield-dialogue>=0.24.0",
    ],
    extras_require={
        "audio": [
            "simpleaudio>=1.0.1",
        ],
        "dev": [
            "Pillow>=7.1.2",
        ],
    },
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "bluemonday-web = bluemonday78.main:run",
        ],
    }
)
