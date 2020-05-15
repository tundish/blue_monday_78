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

Ray does the paperwork
----------------------

.. Ray gives the PC a mission (find out what Martin's up to).

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
