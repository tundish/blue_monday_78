..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-25

.. entity:: NARRATOR
   :types: bluemonday78.logic.Narrator

.. entity:: HERO
   :types: bluemonday78.logic.Player
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

.. entity:: HIPSTER
   :types: bluemonday78.logic.Hipster
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern
            19780118

.. entity:: BARMAN
   :types: bluemonday78.logic.Barman
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_1
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_2
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

Desparation
~~~~~~~~~~~

A pub in Shepherd's Bush
------------------------

[NARRATOR]_

    The wallpaper is scarred, grimy, and punctuated by a diverse collection
    of framed posters.

    Bills for boxing promotions. Flyers for striptease nights.

    Here and there the signed photo of a local celebrity.

    And one, incongruously, of a stricken cargo vessel run recently aground.

[HERO]_

    If you can't get rid of the family skeleton, you may as well
    make it dance.

[BARMAN]_

    Quite so.

[HIPSTER]_

    Why didn't I think of that?

[BARMAN]_

    Maybe you need to read a little wider.

[HIPSTER]_

    I need to put out some of my own records.

    Do you have a function room, |BARMAN_FIRSTNAME|?

[BARMAN]_

    We have a skittle alley out the back. It's for hire at a reasonable
    rate. 

[HIPSTER]_

    I'm going to put on some live acts.

[BARMAN]_

    Oh no, hang on, |HIPSTER_FIRSTNAME|. We have a very strict policy
    when it comes to entertainment.

[HIPSTER]_

    I'm thinking, three bands. Punk or ska.

[BARMAN]_

    Punk or ...?

[HIPSTER]_

    I'll do a tape of the gig and have it cut to flexidisc.

[BARMAN]_

    No, I'm sorry, |HIPSTER_FIRSTNAME|. That's not going to fly.

[HIPSTER]_

    Maybe I could get an old warehouse or an empty factory.

[BARMAN]_

    I tell you what. I can hook you up with beverages.
    I'll do you a good price on Babycham, sale or return.

.. property:: HIPSTER.state 19780119
.. property:: NARRATOR.state 19780119
.. property:: HERO.state bluemonday78.logic.Spot.w12_latimer_arches

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
