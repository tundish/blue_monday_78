import collections
import datetime
import enum
import itertools

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.types import DataObject
from turberfield.dialogue.types import EnumFactory
from turberfield.dialogue.types import Persona
from turberfield.dialogue.types import Player
from turberfield.dialogue.types import Stateful

from bluemonday78 import __version__ as version
from bluemonday78.associations import Associations
from bluemonday78.test.paths import GoldenPath

class Attitude(EnumFactory, enum.Enum):
    neutral = 0
    grumpy = 1
    affable = 2

class Spot(EnumFactory, enum.Enum):
    w12_ducane_prison = "gcpv4d"
    w12_ducane_prison_visiting = "gcpv4d252v5y"
    w12_ducane_prison_release = "gcpv4d1qmdzb"
    w12_ducane_prison_wing = "gcpv4d675t07"
    w12_goldhawk_cafe = "gcpufzg2512x"
    w12_goldhawk_tavern = "gcpufzbd8x5d"
    w12_latimer_arches = "gcpv4cxb3dh4"

class Via(EnumFactory, enum.Enum):
    block = 0
    forwd = 1
    bckwd = 2
    bidir = 3

class Narrator(Stateful): pass
class PrisonOfficer(Stateful, Persona): pass
class Prisoner(Stateful, Persona): pass
class PrisonVisitor(Stateful, Persona): pass
class Barman(Stateful, Persona): pass
class Hipster(Stateful, Persona): pass
class Character(Stateful, Persona): pass
class Location(Stateful, DataObject): pass


blue_monday = datetime.date(1978, 1, 16)


def associations():
    rv = Associations()
    rv.register(
        None,
        *(i.set_state(int(blue_monday.strftime("%Y%m%d")))
          for i in (
            Narrator().set_state(Spot.w12_ducane_prison_visiting),
            Player(name="Mr Likely Story").set_state(Spot.w12_ducane_prison),
            Barman(
                name="Mr Barry Latimer"
            ).set_state(
                Attitude.neutral
            ).set_state(
                Spot.w12_goldhawk_tavern
            ),
            Hipster(name="Mr Justin Cornelis Delcroix").set_state(
                Spot.w12_goldhawk_tavern),
            PrisonOfficer(name="Mr Ray Farington").set_state(Spot.w12_ducane_prison_visiting),
            Prisoner(name="Mr Martin Sheppey").set_state(Spot.w12_ducane_prison),
            PrisonVisitor(name="Mrs Karen Sheppey").set_state(Spot.w12_ducane_prison),
            Character(name="Mr Ian Thomas").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Mike Phillips").set_state(Spot.w12_goldhawk_tavern),
            Character(name="Mr Matthew Waladli").set_state(Spot.w12_goldhawk_tavern),
          )
        ),
        Location(label="Addison Arches 18A").set_state(Spot.w12_latimer_arches),
        Location(label="Wormwood Scrubs").set_state(Spot.w12_ducane_prison),
        Location(label="Wormwood Scrubs visiting").set_state(Spot.w12_ducane_prison_visiting),
        Location(label="Wormwood Scrubs reception").set_state(Spot.w12_ducane_prison_release),
        Location(label="Wormwood Scrubs prison wing").set_state(Spot.w12_ducane_prison_wing),
    )
    return rv

references = list(associations().ensemble()) + [Attitude, Spot, Via]


local = SceneScript.Folder(
    pkg="bluemonday78",
    description="Location-specific elaboration.",
    metadata=[blue_monday],
    paths=[
        "w12_19780116_local/w12_latimer_arches_19780116.rst",
        "w12_19780116_local/w12_latimer_arches_19780117.rst",
    ],
    interludes=itertools.repeat(None)
)


justin = SceneScript.Folder(
    pkg="bluemonday78",
    description="Justin Delcroix has just got the sack.",
    metadata=[blue_monday],
    paths=[
        "justin_19780116_fired/sorrows.rst",
        "justin_19780116_fired/anguish.rst",
        "justin_19780116_fired/desparation.rst"
    ],
    interludes=itertools.repeat(None)
)

ray = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/admin.rst",
        "ray_19780116_retires/escape.rst",
        "ray_19780116_retires/homecoming.rst",
    ],
    interludes=itertools.repeat(None)
)

fade_in = SceneScript.Folder(
    pkg="bluemonday78",
    description="It's Ray Farington's last day.",
    metadata=[blue_monday],
    paths=[
        "ray_19780116_retires/step_forward.rst",
    ],
    interludes=itertools.repeat(GoldenPath.listen_to_karen)
)
plotlines = (justin, ray)
schedule = collections.deque([local])
schedule.extendleft(plotlines)
