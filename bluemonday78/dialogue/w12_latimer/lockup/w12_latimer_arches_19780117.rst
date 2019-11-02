..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-27

.. entity:: HERO
   :types: bluemonday78.types.Player

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_latimer_arches
            19780117

Addison Arches
~~~~~~~~~~~~~~

Day Two
-------

[NARRATOR]_

    The sleeping figure of |HERO_FIRSTNAME| |HERO_SURNAME| lies the
    length of the office floor.

    Camera pulls out through the internal window and rotates to present the
    dusty interior of 18 Addison Arches.

[NARRATOR]_

    The cage contains tumbled stacks of consumer items in their retail
    packaging.

[NARRATOR]_

    Camera walks forward towards the main doors under which light is showing.

    Electrical junction boxes to the left are rusty and have been stripped
    of their cabling.

[NARRATOR]_

    But scaffolding to the right on the wall is new.

    Camera follows the length of it back again and tracks upwards. It is well
    put together and forms a mezzanine to the warehouse.

    There are crates of engineering components and pallets of metal stock.

    Camera centres on one of these as it passes. It is labelled 'INOR-8'.

.. property:: NARRATOR.state 19780118
.. property:: HERO.state bluemonday78.types.Spot.w12_goldhawk_tavern

.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
