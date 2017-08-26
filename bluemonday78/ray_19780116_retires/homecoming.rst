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

[NARRATOR]_

    The rain has been falling since dawn.
    |HERO_FIRSTNAME| |HERO_SURNAME| peers out from the lockup.

    In a curve which follows the arches themselves, a motley array
    of vehicles is parked up all the way down the track which leads
    to the breaker's yard at the end.

[NARRATOR]_

    A solitary figure is at work. In no hurry, he is making his
    way along the line of cars. He stops at each one to peer inside.

[NARRATOR]_

    He turns away from the weather and reaches inside his overcoat to
    something concealed inside.

    Is he making notes?

    He is in uniform.

[OFFICER]_

    Interesting.

.. property:: OFFICER.state 19780119

.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
