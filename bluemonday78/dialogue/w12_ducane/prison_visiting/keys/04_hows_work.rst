..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. entity:: WIFE
   :types: bluemonday78.types.PrisonVisitor

.. entity:: HUSBAND
   :types: bluemonday78.types.Prisoner

   A small-time offender in his mid forties.

    * Can't read. Dislocated.
    * Does what he's told. Wants a quiet life.
    * Misbehaved at Standford Hill to see less of |WIFE|.

.. entity:: HERO
   :types: bluemonday78.types.Player
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen talks of her work
-----------------------


[WIFE]_

    Mandy left finally, and we had a move round.
    So I've got the chair by the window now.

[HUSBAND]_

    Yeah.

[WIFE]_

    Which I like, but in the summer you get the sun right on you.

    When the drier's on that's too much.

[HUSBAND]_

    Yeah.

[WIFE]_

    And wintertime the cold comes straight through the glass.

    So for that I have my cardie.

[HUSBAND]_

    Oh.

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


[HUSBAND]_

    . . .

    So now you're working at the fair?


[WIFE]_

    No, |HUSBAND_FIRSTNAME| I work at Sandy Hair.

    Next to the fair.

[HUSBAND]_

    I thought you said you worked at the fair.

    Did you get sacked from the cleaning?

[WIFE]_

    No, I still do the cleaning.

.. |HUSBAND_FIRSTNAME| property:: HUSBAND.name.firstname
.. |WIFE| property:: WIFE.name.firstname
