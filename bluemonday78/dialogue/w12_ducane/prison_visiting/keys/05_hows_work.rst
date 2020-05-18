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

    Mandy's gone to have her baby, so we had a move around.

    So now I've got the best chair right by the window.

[HUSBAND]_

    Yeah.

[WIFE]_

    About time too.

    You do get the cold come through the glass though.


[HUSBAND]_

    Yeah.

A bit cold though
-----------------

[WIFE]_

    So I've been wearing my cardie, and its a devil to get the hair off it.

[HUSBAND]_

    Oh.

It was my turn
--------------

[WIFE]_

    And the wind comes under the door.

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
