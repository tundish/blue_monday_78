..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |HERO| property:: HERO.name.firstname
.. |WIFE| property:: WIFE.name.firstname
.. |HUSBAND| property:: HUSBAND.name.firstname

.. entity:: WIFE
   :types: bluemonday78.types.PrisonVisitor
   :states: 1

   A beautician in her late forties.

    * Works in `Sandy Hair`, Leysdown-on-Sea.
    * Very organised.
    * Has always looked after |HUSBAND|.

.. entity:: HUSBAND
   :types: bluemonday78.types.Prisoner

   A small-time offender in his mid forties.

    * Can't read. Dislocated.
    * Does what he's told. Wants a quiet life.
    * Misbehaved at Standford Hill to see less of |WIFE|.

.. entity:: HERO
   :types: bluemonday78.types.Player
   :states: bluemonday78.types.Spot.w12_ducane_prison_release

   The player entity.

.. entity:: NARRATOR
   :types: bluemonday78.types.Narrator

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
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
.. |WIFE_TITLE| property:: WIFE.name.title
.. |WIFE_SURNAME| property:: WIFE.name.surname
