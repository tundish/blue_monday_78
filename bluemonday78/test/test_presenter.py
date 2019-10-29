import itertools
import unittest

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
from turberfield.dialogue.types import Player

class SceneTests(unittest.TestCase):

    def setUp(self):
        self.folders = [
            SceneScript.Folder(
                pkg="bluemonday78",
                description="A Spike for Folder patterns.",
                metadata={"location": "inner"},
                paths=[
                    "dialogue/outer/inner/scene_01.rst",
                ],
                interludes=itertools.repeat(None)
            )
        ]
        self.ensemble = [
            Player(name="A Test Actor").set_state(10)
        ]

    def test_folders(self):
        performer = Performer(self.folders, self.ensemble)
        print(*list(performer.run()), sep="\n")
