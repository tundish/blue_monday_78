..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-25

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern
            197801161

.. entity:: HIPSTER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Trade.merchant
            bluemonday78.types.Spot.w12_goldhawk_tavern
            3

.. entity:: BARMAN
   :roles:  FRIENDLY
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Trade.innkeeper
            bluemonday78.types.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_1
   :roles:  FRIENDLY
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_2
   :roles:  FRIENDLY
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern

.. entity:: FRIENDLY
   :roles:  BARMAN
            DRINKER_1
            DRINKER_2
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern
            1

Prospects
~~~~~~~~~

This script plays at:

* 197801161300
* 197801161600
* 197801161900

A pub in Shepherd's Bush
------------------------

[DRINKER_1]_

    Ha ha ha ha!

[NARRATOR]_

    The wallpaper is scarred, grimy, and punctuated by a diverse
    collection of framed posters.

    Bills for boxing promotions. Flyers for striptease nights.

    Here and there the signed photo of a local celebrity.

    And one, incongruously, of a stricken cargo vessel run recently
    aground.

Not what I asked for
--------------------

.. condition:: NARRATOR.state 197801161900

[HIPSTER]_

    So the coach turned up covered in England flags and smelling of sick.

[FRIENDLY]_

    So that's why you got the sack then.

[HIPSTER]_

    Not what Elvis Costello wanted at all.

Needs to make his mark
----------------------

.. condition:: NARRATOR.state 197801161300

[HIPSTER]_

    What I need is to get some band nights going.

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

What about premises?
--------------------

[DRINKER_1]_

    Plenty of empty places around here. You won't have to pay
    anyone if you use one of the factories down the road.

[DRINKER_2]_

    I'd pick one with a roof, though.

[DRINKER_1]_

    Ha ha ha ha!

[HIPSTER]_

    Yeah, I could get an old warehouse or something.

Who's doing your catering?
--------------------------

.. condition:: NARRATOR.state 197801161600

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

What's your poison?
-------------------

.. condition:: NARRATOR.state 197801161900

[NARRATOR]_

    |BARMAN_FIRSTNAME| returns with two bottles and places them
    triumphantly on the counter top. One is very small, and the other
    rather large.

[BARMAN]_

    You've got Natch for the boys, and for the punk ladies, a
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

You're avin' a laugh
--------------------

[DRINKER_1]_

    Ha ha ha ha!

.. property:: FRIENDLY.state 2
.. property:: HIPSTER.state 2
.. property:: NARRATOR.clock 2

Time please
-----------

.. condition:: NARRATOR.state 197801162100

.. property:: NARRATOR.state 197801170815


.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
