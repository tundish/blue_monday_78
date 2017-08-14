..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-19

.. entity:: NOTES
   :types: bluemonday78.logic.Narrator

.. entity:: HIPSTER
   :types: bluemonday78.logic.Hipster
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern
            19780117

.. entity:: BARMAN
   :types: bluemonday78.logic.Barman
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_1
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

.. entity:: DRINKER_2
   :states: bluemonday78.logic.Spot.w12_goldhawk_tavern

Anguish
~~~~~~~

A pub in Shepherd's Bush
------------------------

[NOTES]_

    The head and shoulders of |BARMAN_FIRSTNAME| |BARMAN_SURNAME| rise
    slowly above the level of the counter top. He is negotiating the
    cellar steps at a resigned pace.

    His gaze is attracted, like a magpie, to an object on the bar. It is
    the well-stuffed wallet of |HIPSTER_FIRSTNAME| |HIPSTER_SURNAME|.

[BARMAN]_

    Get you another double, er...

[HIPSTER]_

    |HIPSTER_FIRSTNAME|.

[BARMAN]_

    There you go, |HIPSTER_FIRSTNAME|. That'll be one pound exactly.

[HIPSTER]_

    Nice one, geezer.

[BARMAN]_

    Thankyou.

[DRINKER_1]_

    Ha ha ha ha!

    Oh, look out.

    We could have a Mockney on our hands.

[DRINKER_2]_

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

    You're not going to get any money out of my Uncle. He's not doing too well
    these days.

[BARMAN]_

    Sorry to hear that, |HIPSTER_FIRSTNAME|. Hope he gets better soon.

[HIPSTER]_

    No, I mean the business is in trouble. We didn't know until recently.

    I came here on a course originally. My tuition fees went up last year
    and he said he couldn't pay them any more.

    So I dropped out.

[BARMAN]_

    What course was that then; music?

[HIPSTER]_

    No, I was doing Banking and International Finance.

[DRINKER_1]_

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

[BARMAN]_

    I'm very sorry, |DRINKER_2_FIRSTNAME|, but I'm going to need to see some
    cash this evening.

[HIPSTER]_

    Not banking. Which is just...

[DRINKER_2]_

    Oh behave, |BARMAN_FIRSTNAME|. I'm a loyal customer.

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

[BARMAN]_

    I am saying this for your own good. It's not me who comes to collect if
    you're late.

    You do not want to find yourself in that spot, |DRINKER_2_FIRSTNAME|.

[HIPSTER]_

    It's okay. I'll get these.

[BARMAN]_

    Well that's very good of you, |HIPSTER_FIRSTNAME|.

[DRINKER_2]_

    Too right.

[DRINKER_1]_

    Ha ha ha ha!

.. |BARMAN_FIRSTNAME| property:: BARMAN.name.firstname
.. |BARMAN_SURNAME| property:: BARMAN.name.surname
.. |DRINKER_2_FIRSTNAME| property:: DRINKER_2.name.firstname
.. |HIPSTER_FIRSTNAME| property:: HIPSTER.name.firstname
.. |HIPSTER_SURNAME| property:: HIPSTER.name.surname
