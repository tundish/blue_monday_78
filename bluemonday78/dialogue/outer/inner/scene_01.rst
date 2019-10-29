..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2019-09-29
:project: bluemonday78
:version: |VERSION|

.. entity:: VOICE
   :types: turberfield.dialogue.types.Player
   :states: 1

Scene One
~~~~~~~~~

Scene level text.

Prologue
--------

[VOICE]_

    Hello from |VOICE_SURNAME|.

Option 0
--------

.. condition:: VOICE.state 10

[VOICE]_

    Off.

Option 1
--------

.. condition:: VOICE.state 11

[VOICE]_

    On.

Epilogue
--------

[VOICE]_

    Goodbye from |VOICE_SURNAME|.

.. property:: VOICE.state 20

.. |VOICE_SURNAME| property:: VOICE.name.surname
