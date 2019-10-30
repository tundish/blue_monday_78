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

.. fx:: bluemonday78.static.image location_01.jpg
   :offset: 0
   :duration: 1000
   :loop: 1

.. fx:: bluemonday78.static.image location_02.jpg
   :offset: 1000
   :duration: 1000
   :loop: 1

.. fx:: bluemonday78.static.image location_03.jpg
   :offset: 3000
   :duration: 20000
   :loop: 1


[VOICE]_

    Hello from |VOICE_SURNAME|.

Option 0
--------

.. condition:: VOICE.state 10

[VOICE]_

    On.

Option 1
--------

.. condition:: VOICE.state 11

[VOICE]_

    Off.

Epilogue
--------

[VOICE]_

    Goodbye from |VOICE_SURNAME|.

.. property:: VOICE.state 20

.. fx:: bluemonday78.static.audio  transition_01.mp3
   :offset: 0
   :duration: 19513
   :loop: 1


.. |VOICE_SURNAME| property:: VOICE.name.surname
