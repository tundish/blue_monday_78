..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |WIFE| property:: WIFE.name.firstname
.. |HUSBAND| property:: HUSBAND.name.firstname

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting
            197801160810

.. entity:: WIFE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.healer
            bluemonday78.types.Spot.w12_ducane_prison_visiting
            1

.. entity:: HUSBAND
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.mug
            bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_release
            bluemonday78.types.Mode.guardian


In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen talks of the journey
--------------------------

.. fx:: bluemonday78 karen/rejects-01.jpg
   :offset: 0
   :duration: 30
   :loop: 1

.. fx:: bluemonday78 karen/rejects-02.jpg
   :offset: 0
   :duration: 30
   :loop: 1

[NARRATOR]_

    The Visiting Suite is a long hall with small tables arranged
    in a grid.

Tables
------

[HUSBAND]_

    Got to be careful. Looks like we've got the Book.

[WIFE]_

    The what?

[HUSBAND]_

    That's |OFFICER_SURNAME| outside. They call him the Book.
    He's a total loony.

[WIFE]_

    Oooh, we can choose our own table today!

[HUSBAND]_

    No, let's sit here again.

Too early
---------

[WIFE]_

    I don't like visiting time so early. There's traffic now on the M2.

[HUSBAND]_

    Yeah.

[WIFE]_

    But it's not so bad later on.

[HUSBAND]_

    No.

[WIFE]_

    Mid morning's okay. I sometimes go with the girls for lunch at Farthing Corner.

    Which is nice.

[HUSBAND]_

    Oh.

Why here?
---------

[WIFE]_

    I really don't know why they had to move you up here. Standford Hill was much
    easier.

[HUSBAND]_

    Yeah, easier, but...

[WIFE]_

    And this place is full of hard nuts. Why did they think you belonged here? You were
    close to coming out, too.

[HUSBAND]_

    No, it's...

    A shame.

.. property:: WIFE.state 2

.. |HUSBAND_FIRSTNAME| property:: HUSBAND.name.firstname
.. |WIFE_TITLE| property:: WIFE.name.title
.. |WIFE_SURNAME| property:: WIFE.name.surname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
