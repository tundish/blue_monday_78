from collections import namedtuple
import itertools
import unittest

from turberfield.dialogue.model import Model
from turberfield.dialogue.model import SceneScript
from turberfield.dialogue.performer import Performer
from turberfield.dialogue.types import Player
from turberfield.utils.misc import group_by_type


class Presenter:
    """
        #. Display every shot in its entirety. Never split a shot.
        #. Shot renders; images, audio, dialogue.
        #, Delay and duration for each line of dialogue
        #, Offset and duration for each Static
        #. Refresh media for multishot scenes.
    """

    Animation = namedtuple("Animation", ["delay", "duration", "element"])

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

    def __init__(self, dialogue):
        self.frames = [group_by_type(i.items) for i in dialogue.shots]

    @property
    def pending(self):
        return len([
            frame for frame in self.frames
            if all([Performer.allows(i) for i in frame[Model.Condition]])
        ])

    def frame(self, dwell=0.3, pause=1, react=True):
        while True:
            frame = self.frames.pop(0)
            if all([Performer.allows(i) for i in frame[Model.Condition]]):
                for p in frame[Model.Property]:
                    if react and p.object is not None:
                        setattr(p.object, p.attr, p.val)
                return frame

class SceneTests(unittest.TestCase):

    def setUp(self):
        self.folders = [
            SceneScript.Folder(
                pkg="bluemonday78",
                description="A Spike for Folder patterns.",
                metadata={"location": "inner"},
                paths=[
                    "dialogue/outer/inner/story/scene_01.rst",
                ],
                interludes=itertools.repeat(None)
            )
        ]
        self.ensemble = [
            Player(name="A Test Actor").set_state(10)
        ]

    def test_frame(self):
        dialogue = Presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        shot_index = 0
        self.assertEqual(10, self.ensemble[0].state)
        while presenter.pending:
            with self.subTest(shot_index=shot_index):
                frame = presenter.frame()
                self.assertTrue(frame)
                shot_index += 1
        self.assertEqual(3, shot_index)
        self.assertEqual(20, self.ensemble[0].state)

    def test_prologue(self):
        dialogue = Presenter.dialogue(self.folders, self.ensemble)
        presenter = Presenter(dialogue)
        print(*presenter.frames, sep="\n")
