..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-27

.. entity:: HERO
   :types: bluemonday78.logic.Player

.. entity:: DAY_01
   :types:  bluemonday78.logic.Narrator
   :states: bluemonday78.logic.Spot.w12_latimer_arches
            19780116

.. entity:: DAY_02
   :types:  bluemonday78.logic.Narrator
   :states: bluemonday78.logic.Spot.w12_latimer_arches
            19780117

.. entity:: DAY_03
   :types:  bluemonday78.logic.Narrator
   :states: bluemonday78.logic.Spot.w12_latimer_arches
            19780118

Addison Arches
~~~~~~~~~~~~~~

Day 01
------

[DAY_01]_

    Birdsong. A sparrow is perched on the rim of a latrine.

    Pull back through the splintered roof of a wooden cabin in the yard
    alongside Addison Arches.

.. property:: DAY_01.state 19780117

Day 02
------

[DAY_02]_

    The sleeping figure of |HERO_FIRSTNAME| |HERO_SURNAME| lies the
    length of the office floor.

    Pull out through the internal window and rotate to present the dusty
    interior of 18 Addison Arches.

[DAY_02]_

    The cage contains tumbled stacks of consumer items in their retail
    packaging.

[DAY_02]_

    Walk forward towards the main doors under which light is showing.

    Electrical junction boxes to the left are rusty and have been stripped
    of their cabling.

[DAY_02]_

    But scaffolding to the right on the wall is new.

    Follow the length of it back again and rise upwards. It is well put
    together and forms a mezzanine to the warehouse.

    There are crates of engineering components and pallets of metal stock.

    We pass label after label. They all say 'INOR-8'.

.. property:: DAY_02.state 19780118

Day 03
------

[DAY_03]_

    Day three.

.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
