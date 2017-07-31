import sys

from cx_Freeze import setup
from cx_Freeze import Executable

import turberfield

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = {
    "packages": [
        "asyncio.base_subprocess", "asyncio.constants", "asyncio.compat",
        "asyncio.selector_events",
        "six",
        "blessings", "turberfield.dialogue",
        "bluemonday78",
    ],
    "namespace_packages": ["turberfield"],
    "includes": [],
    "excludes": []
}

base = "Win32GUI" if sys.platform=="win32" else None

executables = [
    Executable("bluemonday78/main.py", base=base)
]

setup(
    name="bluemonday78",
    version="1.0",
    description="",
    options={
        "build_dmg": buildOptions,
        "build_exe": buildOptions,
    },
    executables=executables
)
