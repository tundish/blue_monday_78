import sys

from cx_Freeze import setup
from cx_Freeze import Executable

import turberfield

buildOptions = {
    "packages": [
        "asyncio.base_subprocess", "asyncio.constants", "asyncio.compat",
        "asyncio.selector_events",
        "pkg_resources._vendor.six", "pkg_resources._vendor.appdirs",
        "pkg_resources._vendor.packaging", "pkg_resources._vendor.pyparsing",
        "blessings", "turberfield.dialogue",
        "bluemonday78",
    ],
    "namespace_packages": ["turberfield"],
    "includes": [],
    "excludes": []
}

if sys.platform == "win32":
    base = "Win32GUI"
elif sys.platform == "darwin":
    base = None
    buildOptions["packages"].append("_sysconfigdata_m_darwin_darwin")
else:
    base = None

if sys.version_info.major != 3:
    print("Supports Python 3 only.")
    sys.exit(1)

if sys.version_info.minor > 5:
    buildOptions["packages"].extend([
        "asyncio.base_futures", "asyncio.base_tasks",
    ])

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
