..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |INMATE| property:: INMATE.name.firstname

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.guardian
            bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: VISITOR
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.healer
            bluemonday78.types.Spot.w12_ducane_prison_visiting
            4

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief
            bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: CELLMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.mug
            bluemonday78.types.Spot.w12_ducane_prison_visiting

Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray bestows a parting gift
--------------------------

[NARRATOR]_

    The Guard's Room is a shabby little office. There are some filing cabinets and a couple
    of chairs.

    Everything is painted a thick institutional green.

[OFFICER]_

    Good Lord, what a mess. I'm the only one who tidies this place up.

[NARRATOR]_

    Someone has been throwing sharpened pencils at the suspended ceiling. Two or
    three are stuck into the soft board and are just within reach.

[NARRATOR]_

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| pulls something out of a box near the floor.
    He looks at it for a moment.

[OFFICER]_

    You may as well have this. It's not doing any good in here.

[NARRATOR]_

    |OFFICER_SURNAME| tosses onto the desk a small book of thick waxy paper.

    Its cover is of stiffened cloth.

    It is held together by a shoelace.

Ray shares a memory
-------------------

[OFFICER]_

    I would always issue these to my squad leaders. I used to train them
    to make a note of everything they saw.

[INMATE]_

    Thanks, |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Can't give you a pen I'm afraid.

[INMATE]_

    That's okay, |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Help yourself to a pencil, though.

Ray does the paperwork
----------------------


[OFFICER]_

    Well, now, let's have you on your way.
    It's a funny thing. This happens to be my last day as well.
    I'm about to take early retirement.

    After thirty years. I came straight out of the Army into the Prison Service.

    So at least we have this in common; neither of us can wait to get out of here! 

[NARRATOR]_

    Martin and Karen's argument has become very loud.

[OFFICER]_

    There's never enough time is there, to say what we have to. But I'd like
    you to know I've been impressed by your influence on |CELLMATE_FIRSTNAME| |CELLMATE_SURNAME|.
    His literacy is very much improved. And he's been practicing his handwriting too, I understand.

[NARRATOR]_

    There is cursing and screaming.

[OFFICER]_

    And I know why that is. You didn't start out with many options in life.
    We know you have a difficult family background.

    Most people don't recover from such a beginning. Except, you have a very special
    kind of tenacity. You don't give up, do you?

    I'd just like you to know, that I admire your attitude. Although I can see it might
    lead to more trouble if you're not careful.

[NARRATOR]_

    An alarm bell rings.

.. property:: NARRATOR.state 197801161100
.. property:: INMATE.state bluemonday78.types.Spot.w12_latimer_arches

.. |INMATE_TITLE| property:: INMATE.name.title
.. |INMATE_SURNAME| property:: INMATE.name.surname
.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
