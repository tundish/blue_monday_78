..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-19

.. entity:: NOTES
   :types: logic.Narrator

.. entity:: HIPSTER
   :types: logic.Hipster
   :states: logic.Spot.w12_goldhawk_tavern

.. entity:: BARMAN
   :types: logic.Barman
   :states: logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_1
   :states: logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_2
   :states: logic.Spot.w12_goldhawk_tavern

Anguish
~~~~~~~

A pub in Shepherd's Bush
------------------------

[NOTES]_

    The head and shoulders of |BARMAN_FIRSTNAME| |BARMAN_SURNAME| rise
    slowly above the level of the counter top. He emerges up the cellar
    steps at a resigned pace.

    His eyes are drawn, like a magpie's to an object on the bar. It is
    the well-stocked wallet of |HIPSTER_FIRSTNAME| |HIPSTER_SURNAME|.

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |BARMAN_SURNAME| property:: BARMAN.name.surname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HIPSTER_SURNAME| property:: HIPSTER.name.surname
