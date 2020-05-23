..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-19

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_goldhawk_tavern
            197801161

.. entity:: HIPSTER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.yuppie
            bluemonday78.types.Spot.w12_goldhawk_tavern
            2

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

Family
~~~~~~

This script plays at:

* 197801161200
* 197801161500
* 197801161800

Up from the depths
------------------

.. condition:: NARRATOR.state 197801161200

[NARRATOR]_

    The head and shoulders of |BARMAN_FIRSTNAME| |BARMAN_SURNAME| rise
    slowly above the level of the counter top. He is negotiating the
    cellar steps at a steady pace.

A better class of customer
--------------------------

.. condition:: NARRATOR.state 197801161500

[NARRATOR]_

    |BARMAN_FIRSTNAME|'s gaze is attracted, like a magpie, to an object on the bar. It is
    the well-stuffed wallet of |HIPSTER_FIRSTNAME| |HIPSTER_SURNAME|.

Justin pipes up
---------------

[HIPSTER]_

    I used to be in the music industry.

    Until this morning.

    I'm celebrating being unemployed.

[FRIENDLY]_

    Oh dear. Did they pay you off though?

[HIPSTER]_

    Yes, I've got it right here.

[FRIENDLY]_

    Ah, good.
 
Hospitality
-----------

[BARMAN]_

    Get you another double, er...

[HIPSTER]_

    |HIPSTER_FIRSTNAME|.

[BARMAN]_

    There you go, |HIPSTER_FIRSTNAME|. That'll be one pound exactly.

[HIPSTER]_

    And one for yourself.

[BARMAN]_

    Thankyou.

Just a tourist
--------------

.. condition:: NARRATOR.state 197801161200

[FRIENDLY]_

    You're not from around here, are you, son.

[HIPSTER]_

    No, actually.

Where you from?
---------------

.. condition:: NARRATOR.state 197801161500

[FRIENDLY]_

    Where's home for you then, |HIPSTER_FIRSTNAME|?

[HIPSTER]_

    Well, I grew up in Antigua, as it happens.

[DRINKER_2]_

    Where?

What's your name?
-----------------

.. condition:: NARRATOR.state 197801161800

[HIPSTER]_

    My family are...

    Have you heard of |HIPSTER_SURNAME|?

[NARRATOR]_

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

Global downturn
---------------

[HIPSTER]_

    You're not going to get any money out of my Uncle. He's not doing too well
    these days.

[BARMAN]_

    Sorry to hear that, |HIPSTER_FIRSTNAME|. Hope he gets better soon.

[HIPSTER]_

    No, I mean the business is in trouble. We didn't know until recently.

    I came here on a course to begin with. My tuition fees went up last year
    and he said he couldn't pay them any more.

    So I dropped out.

No money
--------

[FRIENDLY]_

    What course was that then; music?

[HIPSTER]_

    No, I was doing Banking and International Finance.

[FRIENDLY]_

    Stone me.

[HIPSTER]_

    At City University. So then I dropped out. And it's not the right time
    to go back home just now because everyone's at each other's throats over
    the liquidation.

[DRINKER_2]_

    Liquid nation.

[DRINKER_1]_

    Ha ha ha ha!

[HIPSTER]_

    So I got the job at the record company.

[DRINKER_2]_

    Yes please, |BARMAN_FIRSTNAME|.

[HIPSTER]_

    And then I realised that I wanted to be in music.

Pay me
------

.. condition:: NARRATOR.state 197801161200

[BARMAN]_

    I'm very sorry, |DRINKER_2_FIRSTNAME|, but I'm going to need to see some
    cash this week.

[HIPSTER]_

    Not banking. Which is just...

[DRINKER_2]_

    Oh behave, |BARMAN_FIRSTNAME|. I'm a loyal customer.

Seriously, pay me
-----------------

.. condition:: NARRATOR.state 197801161500

[BARMAN]_

    |DRINKER_2_FIRSTNAME|, my business partners recognise the importance of
    retaining loyal customers, which is why they allow me to operate a slate.

    They understand that a working man can have cashflow problems now and then.

[DRINKER_2]_

    I am not some fucking mug.

[BARMAN]_

    They do get concerned |DRINKER_2_FIRSTNAME|, when that gentleman makes no
    attempt to reduce his obligations after a period of one calendar month.

    And you know that, because we have had this conversation before.

[DRINKER_2]_

    Oh come on, |BARMAN_FIRSTNAME|!

The kindness of strangers
-------------------------

.. condition:: NARRATOR.state 197801161800

[BARMAN]_

    I am saying this for your own good. It's not me who comes to collect if
    you're late.

    You do not want to find yourself in that situation, |DRINKER_2_FIRSTNAME|.

[HIPSTER]_

    It's okay. I'll get these.

[BARMAN]_

    Well that's very good of you, |HIPSTER_FIRSTNAME|.

[DRINKER_2]_

    Too right.

[DRINKER_1]_

    Ha ha ha ha!

He's on the phone
-----------------

.. condition:: NARRATOR.state 197801161500

[HIPSTER]_

    They told me to go out and hire a tour bus.

    It was all very last minute.

[FRIENDLY]_

    Did you look in the Yellow Pages?

[HIPSTER]_

    They only had one phone in the office. You could never get on it.

    So I went round to a place near here. It's on my way home.

What not to do
--------------

.. condition:: NARRATOR.state 197801161500

[HIPSTER]_

    Bulldog coaches, do you know them?

    A guy called Victor Yeoman.

[FRIENDLY]_

    Vic Yeoman.

    His yard is in on Depot Road.

[HIPSTER]_

    That's the one.

There's your mistake
--------------------

.. condition:: NARRATOR.state 197801161800

[BARMAN]_

    Vic does the football tours over to Holland and Spain.

    I don't think you're cut out to be one of his passengers though, to be honest.

[HIPSTER]_

    Do you find him slighty right wing?

[BARMAN]_

    I'd say a bit right wing, yes.

Not what I asked for
--------------------

.. condition:: NARRATOR.state 197801161800

[HIPSTER]_

    So the coach turned up covered in England flags and smelling of sick.

[FRIENDLY]_

    So that's why you got the sack then.

[HIPSTER]_

    Not what Elvis Costello wanted at all.

Always
------

.. property:: HIPSTER.state 3
.. property:: NARRATOR.clock 1

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |BARMAN_SURNAME| property:: BARMAN.name.surname
.. |DRINKER_2_FIRSTNAME| property:: DRINKER_2.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HIPSTER_SURNAME| property:: HIPSTER.name.surname
