import itertools
import unittest

from turberfield.dialogue.model import SceneScript
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


    @staticmethod
    def run(model, react=True):
        for shot, item in model:

            if self.condition is not False:
                yield shot
                yield item

            if not self.shots or self.shots[-1][:2] != shot[:2]:
                self.shots.append(shot._replace(items=self.script.fP))
                self.condition = None

            if isinstance(item, Model.Condition):
                self.condition = self.allows(item)

            if react:
                self.react(item)


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
        print(*dialogue.shots, sep="\n")
