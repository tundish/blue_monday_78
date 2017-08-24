..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-27

.. entity:: HERO
   :types: bluemonday78.logic.Player

.. entity:: NARRATOR
   :types:  bluemonday78.logic.Narrator
   :states: bluemonday78.logic.Spot.w12_latimer_arches
            19780117

Addison Arches
~~~~~~~~~~~~~~

Day Two
-------

[NARRATOR]_

    The sleeping figure of |HERO_FIRSTNAME| |HERO_SURNAME| lies the
    length of the office floor.

    Pull out through the internal window and rotate to present the dusty
    interior of 18 Addison Arches.

[NARRATOR]_

    The cage contains tumbled stacks of consumer items in their retail
    packaging.

[NARRATOR]_

    Walk forward towards the main doors under which light is showing.

    Electrical junction boxes to the left are rusty and have been stripped
    of their cabling.

[NARRATOR]_

    But scaffolding to the right on the wall is new.

    Follow the length of it back again and track upwards. It is well put
    together and forms a mezzanine to the warehouse.

    There are crates of engineering components and pallets of metal stock.

    We glimpse a label as we pass. It says 'INOR-8'.

.. property:: NARRATOR.state 19780118

.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
