..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2018-01-20
:project: bluemonday78
:version: |VERSION|

.. entity:: NARRATOR
   :types: bluemonday78.types.Narrator

.. entity:: OFFICER
   :types: bluemonday78.types.PrisonOfficer
   :states: bluemonday78.types.Spot.w12_ducane_prison_wing

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: CELLMATE
   :types: bluemonday78.types.Prisoner

   A small-time offender in his mid forties.

.. entity:: HERO
   :types: bluemonday78.types.Player

   The player entity.

A Prison Wing
~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.


Ray is on the landing
---------------------

[NARRATOR]_

    We fade in to the sound of keys in an iron door.

[CELLMATE]_

    Off you go then, |HERO_FIRSTNAME|. Looks like you're gonna get the Book.

[HERO]_

    The what?

[CELLMATE]_

    That's |OFFICER_SURNAME| outside. They call him the Book.
    He's a total loony.

    Good luck on the outside.

Ray enters
----------

[OFFICER]_

    Prisoner |HERO_SURNAME| step forward. Prisoner |CELLMATE_SURNAME| step forward.

[CELLMATE]_

    What, me too |OFFICER_TITLE| |OFFICER_SURNAME| ?

[OFFICER]_

    You too, |CELLMATE_SURNAME|. You will vacate this cell immediately. You will
    touch nothing on your way out.

[CELLMATE]_

    But I haven't done anything, |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    This cell is scheduled for a contraband search.

    You will both vacate this cell immediately.

    You will touch nothing on your way out.

[CELLMATE]_

    Yes, |OFFICER_TITLE| |OFFICER_SURNAME|.

[NARRATOR]_

    |CELLMATE_SURNAME| and |HERO_SURNAME| step out of the cell onto the narrow
    balcony.

Ray joins them on the balcony
-----------------------------

[OFFICER]_

    |CELLMATE_SURNAME|, your lady wife has arrived outside. So you will have
    thirty minutes visiting time until 09:00.

    |HERO_SURNAME| you are with me while I sign you off for release.

    Right, now we will proceed in silence to Visiting Suite. At the double!

.. memory:: 197801160800
   :subject: HERO

   |HERO_FIRSTNAME| |HERO_SURNAME| gets out of Prison today.

.. property:: OFFICER.state bluemonday78.types.Spot.w12_ducane_prison_release
.. property:: CELLMATE.state bluemonday78.types.Spot.w12_ducane_prison_visiting
.. property:: HERO.state bluemonday78.types.Spot.w12_ducane_prison_release

.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
