..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-04

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern
            1978011611

.. entity:: HIPSTER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.yuppie
            bluemonday78.types.Spot.w12_goldhawk_tavern
            1

.. entity:: BARMAN
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Trade.innkeeper
            bluemonday78.types.Spot.w12_goldhawk_tavern

Sorrows
~~~~~~~

..  Stiff Records' first office was at 32 Alexander St, Bayswater.
    Quite walkable from Shepherd's Bush.

A pub in Shepherd's Bush
------------------------

[NARRATOR]_

    Monday lunchtime.

    Just two hours ago, Stiff Records fired their most junior runner.

    He ran off with a Sony Pressman TC-D5 and is
    now in the Goldhawk Tavern, Shepherd's Bush.

.. property:: HIPSTER.state 2
.. property:: NARRATOR.clock 1
