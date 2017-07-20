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
    slowly above the level of the counter top. He emerges from the cellar
    steps at a resigned pace.

    His gaze is attracted, like a magpie, to an object on the bar. It is
    the well-stocked wallet of |HIPSTER_FIRSTNAME| |HIPSTER_SURNAME|.

[BARMAN]_

    Get you another double, er...

[HIPSTER]_

    |HIPSTER_FIRSTNAME|.

[BARMAN]_

    There you go, |HIPSTER_FIRSTNAME|. That'll be one pound exactly.

[HIPSTER]_

    Cheers, geezer.

[BARMAN]_

    Thankyou.

[DRINKER_1]_

    Ha ha ha ha!

    Oh, look out.

[DRINKER_2]_

    We could have a Mockney on our hands.

[DRINKER_1]_

    No, I thought Mick Jagger had walked in here for a minute.

[BARMAN]_

    You're not from around here, are you, son.

[HIPSTER]_

    No, actually.

[BARMAN]_

    Where's home for you then, |HIPSTER_FIRSTNAME|?

[HIPSTER]_

    Well, I grew up in Antigua, as it happens.

[DRINKER_2]_

    Where?

[HIPSTER]_

    My family are...

    Have you heard of |HIPSTER_SURNAME|?

[NOTES]_

    Nobody has.

[HIPSTER]_

    Well, I'm |HIPSTER_FIRSTNAME| |HIPSTER_SURNAME|.

    Our family has a shipping business.

    My uncle, really.

[DRINKER_2]_

    Well stroll on. Get the door, |BARMAN_FIRSTNAME|. How much
    shall we ask for ransom?

[DRINKER_1]_

    Ha ha ha ha!

[HIPSTER]_

    You're not going to get any money out of my Uncle these days. He's not
    doing too well. He stopped paying my tuition fees last year and I had
    to drop out of the course I was here for.

[BARMAN]_

    That's a shame, |HIPSTER_FIRSTNAME|.


.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |BARMAN_SURNAME| property:: BARMAN.name.surname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HIPSTER_SURNAME| property:: HIPSTER.name.surname
