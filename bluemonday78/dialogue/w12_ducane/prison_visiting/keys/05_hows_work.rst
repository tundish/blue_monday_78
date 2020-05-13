..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: WIFE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.healer
            bluemonday78.types.Spot.w12_ducane_prison_visiting
            3

.. entity:: HUSBAND
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.mug
            bluemonday78.types.Spot.w12_ducane_prison_visiting

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

A new spot
----------


[WIFE]_

    Mandy's gone now, and we had a move round.
    So I've got the best chair right by the window.

[HUSBAND]_

    Yeah.

[WIFE]_

    Which I like, but in the summer you get the sun right on you.

    And when the drier's on it's worse still.

[HUSBAND]_

    Yeah.

A bit cold though
-----------------

[WIFE]_

    All this week I've been getting the cold coming through the glass.

    So I have to wear my cardie, and it picks up the hair something chronic.

[HUSBAND]_

    Oh.

It was my turn
--------------

[WIFE]_

    And you get the wind through the door.

[HUSBAND]_

    Yep.

[WIFE]_

    And I keep my bag in the back and it's further away now and I can't see it from
    where I am.

[HUSBAND]_

    No.


[WIFE]_

    But I do like it.

    Mandy had it all the time she was there so fair's fair.

Not listening
-------------

[HUSBAND]_

    So now you're working at the fair?


[WIFE]_

    No, |HUSBAND_FIRSTNAME| I work at Sandy Hair.

    Next to the fair.

Still not listening
-------------------

[HUSBAND]_

    I thought you said you worked at the fair.

    Did you get sacked from the cleaning?

[WIFE]_

    No, I still do the cleaning.

.. property:: WIFE.state 2

.. |HUSBAND_FIRSTNAME| property:: HUSBAND.name.firstname
.. |WIFE| property:: WIFE.name.firstname
