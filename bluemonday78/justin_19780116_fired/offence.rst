..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-23

.. entity:: HERO
   :types: logic.Player

.. entity:: BARMAN
   :types:  logic.Barman
   :states: logic.Spot.w12_goldhawk_tavern
            logic.Attitude.grumpy

Offence
~~~~~~~

A pub in Shepherd's Bush
------------------------

[HERO]_

    This is Frankie Marshall's place.

[BARMAN]_

    Aren't you the clever one. Now are you in need of refreshment?

    Because if not, the place for you is outside.

.. property:: BARMAN.state logic.Attitude.neutral
