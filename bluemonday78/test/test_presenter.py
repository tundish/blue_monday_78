import itertools
import unittest

from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
from turberfield.dialogue.types import Player


class Presenter:

    @staticmethod
    def dialogue(folders, ensemble, strict=True, roles=1):
        for folder in folders:
            for script in SceneScript.scripts(**folder._asdict()):
                with script as dialogue:
                    selection = dialogue.select(ensemble, roles=roles)
                    if selection and all(selection.values()):
                        return dialogue.cast(selection).run()
                    elif not strict and any(selection.values()):
                        return dialogue.cast(selection).run()


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
        dialogue = Presenter.dialogue(self.folders, self.ensemble)
        print(*dialogue.scenes, sep="\n")
        print(*dialogue.shots, sep="\n")
        print(Performer.allows)
