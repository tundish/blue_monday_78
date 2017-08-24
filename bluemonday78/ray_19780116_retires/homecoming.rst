..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-23

.. entity:: NARRATOR
   :types:  bluemonday78.logic.Narrator
   :states: bluemonday78.logic.Spot.w12_latimer_arches
            19780119

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: 19780118

.. entity:: HERO
   :types: bluemonday78.logic.Player
   :states: bluemonday78.logic.Spot.w12_latimer_arches

A chance encounter
~~~~~~~~~~~~~~~~~~

Morning outside the warehouse.

On the approach
---------------

.. property:: OFFICER.state bluemonday78.logic.Spot.w12_latimer_arches

[OFFICER]_

    More interesting.

.. property:: OFFICER.state 19780119
