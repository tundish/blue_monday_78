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

[DRINKER_1]_

    Ha ha ha ha!

[NARRATOR]_

    |HERO_FIRSTNAME| |HERO_SURNAME| sits at a small round table in
    the bar of the Goldhawk Tavern. On the floor is an electric heater.

    The wallpaper is scarred, grimy, and punctuated by a diverse
    collection of framed posters.

    Bills for boxing promotions. Flyers for striptease nights.

    Here and there the signed photo of a local celebrity.

    And one, incongruously, of a stricken cargo vessel run recently
    aground.

[HERO]_

    If you can't get rid of the family skeleton, you may as well
    make it dance.

[NARRATOR]_

    It goes quiet for a moment.

[BARMAN]_

    Quite so.

[HIPSTER]_

    Why didn't I think of that?

[BARMAN]_

    Maybe you need to read a little wider.

[HIPSTER]_

    What I need is get some band nights going.

    Do you have a function room, |BARMAN_FIRSTNAME|?

[BARMAN]_

    We have a skittle alley out the back. It's for hire at a reasonable
    rate. 

[HIPSTER]_

    I'm going to put on some live acts. Get a regular thing going.

[BARMAN]_

    Oh no, hang on, |HIPSTER_FIRSTNAME|. We have a very strict policy
    when it comes to entertainment.

[HIPSTER]_

    I'm thinking, three bands. Punk or Ska.

[BARMAN]_

    Punk or ...?

[HIPSTER]_

    I'll do a tape of the gig and have it cut to flexidisc.
    Put it out there. Establish a local scene.

[BARMAN]_

    No, I'm sorry, |HIPSTER_FIRSTNAME|. That's not going to fly.

[DRINKER_1]_

    Plenty of empty places around here. You wouldn't have to pay
    anyone if you used one of the factories down the road.

[DRINKER_2]_

    I'd pick one with a roof, though.

[DRINKER_1]_

    Ha ha ha ha!

[HIPSTER]_

    Yeah, I could get an old warehouse or something.

[BARMAN]_

    Now I tell you what, |HIPSTER_FIRSTNAME|. I can hook you up with
    beverages.

[NARRATOR]_

    |BARMAN_FIRSTNAME| turns and disappears down into the cellar.

[HIPSTER]_

    Beverages?

[NARRATOR]_

    |BARMAN_FIRSTNAME|'s voice floats upward.

[BARMAN]_

    Well those punks of yours are going to want something to drink
    while they're waiting for the Ska to come on.

[HIPSTER]_

    That's not a bad idea.

[NARRATOR]_

    |BARMAN_FIRSTNAME| returns with two bottles and places them
    triumphantly on the counter top. One is very small, and the other
    rather large.

[BARMAN]_

    You've got your Natch for the boys, and for the punk ladies, a
    nice little Babycham.

[HIPSTER]_

    That one looks a bit funny. Is it all right?

[BARMAN]_

    Oh yes. Keeps forever, does Babycham. But they changed the
    label a little while back. These are the old style, that's all.

[DRINKER_2]_

    Do punks drink cider? I thought that was farmers.

[BARMAN]_

    They will love this stuff, I promise you. I can let you have
    two dozen cases of each, sale or return.

[HIPSTER]_

    This is going to work brilliantly.

[DRINKER_1]_

    Ha ha ha ha!

.. property:: HIPSTER.state 19780119
.. property:: NARRATOR.state 19780119
.. property:: HERO.state bluemonday78.logic.Spot.w12_latimer_arches

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HERO_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HERO_SURNAME| property:: HIPSTER.name.surname
