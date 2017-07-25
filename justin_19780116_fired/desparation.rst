..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-25

.. entity:: NOTES
   :types: logic.Narrator

.. entity:: HERO
   :types: logic.Player

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

Desparation
~~~~~~~~~~~

A pub in Shepherd's Bush
------------------------

[HERO]_

    If you can't get rid of the family skeleton, you may as well
    make it dance.

[BARRY]_

    Quite so.

[HIPSTER]_

    Why didn't I think of that? Of course.

    I need to put out some of my own records.

    Do you hava a function room, |BARMAN_FIRSTNAME|?

[BARRY]_

    We have a skittle alley out the back. It's for hire at a reasonable
    rate. 

[HIPSTER]_

    I'm going to put on some live acts.

[BARRY]_

    Oh no, hang on, |HIPSTER_FIRSTNAME|. We have a very strict policy
    when it comes to entertainment.

[HIPSTER]_

    I'm thinking, three bands. Punk or ska.

[BARRY]_

    Punk or...

[HIPSTER]_

    I'll do a tape of the gig and have it cut to flexidisc.

[BARRY]_

    No, I'm sorry, |HIPSTER_FIRSTNAME|. That's not going to run.

[HIPSTER]_

    Maybe I could get an old warehouse or an empty factory.

[BARRY]_

    I tell you what. I can hook you up with beverages.
    I'll do you a good price on Babycham, sale or return.

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
