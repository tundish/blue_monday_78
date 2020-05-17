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

.. entity:: CELLMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief
            bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.guardian

.. entity:: EXIT
   :types:  bluemonday78.types.Location
   :states: bluemonday78.types.Spot.w12_ducane_prison_release

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

[NARRATOR]_

    |INMATE| is hovering in the doorway.

Did not expect that
-------------------

[CELLMATE]_

    |INMATE|, quick. She's only brought the keys with her.

[INMATE]_

    Nice. Couldn't have worked out better.

    Your old dear's on the firm.

[CELLMATE]_

    What if they search her?

[INMATE]_

    Pass them over then.

Martin hands over the keys
--------------------------

[NARRATOR]_

    |CELLMATE| throws |INMATE| the keys.

[INMATE]_

    Saves me a trip.

[NARRATOR]_

    |CELLMATE| eyes |INMATE| nervously.

[CELLMATE]_

    What about the money? You're still going to drop off my money, right?

[INMATE]_

    Yeah but I've got to sell the gear first.

Stand on me
-----------

[CELLMATE]_

    Yeah, clear out all that gear or there won't be room for the new stuff.

[INMATE]_

    Don't worry mate, don't worry.

[CELLMATE]_

    Yeah, well make sure that place is empty soon, or I'm gonna get a hiding!

    And don't let anybody in there.

    And don't mention Frankie Marshall.

.. property:: INMATE.state bluemonday78.types.Spot.w12_ducane_prison_release

.. memory::  bluemonday78.types.Spot.w12_ducane_prison_visiting
   :subject: NARRATOR

   |CELLMATE| passes some keys to |INMATE|.

.. |CELLMATE| property:: CELLMATE.name.firstname
.. |INMATE| property:: INMATE.nickname
