..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2018-01-20
:project: bluemonday78
:version: |VERSION|

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: 197801160800

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_wing
            bluemonday78.types.Mode.guardian

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: CELLMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_wing

   A small-time offender in his mid forties.

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_wing
            bluemonday78.types.Mode.thief

   The player entity.

.. entity:: OBJECTIVE
   :types:  bluemonday78.types.Location
   :states: bluemonday78.types.Spot.w12_ducane_prison_release

A Prison Wing
~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.


Ray is on the landing
---------------------

.. fx:: bluemonday78 ray/approaches-01.jpg
   :offset: 0
   :duration: 30
   :loop: 1

[NARRATOR]_

    The sound of keys in an iron door.

[CELLMATE]_

    Off you go then, |INMATE_FIRSTNAME|. Looks like you're gonna get the Book.

[INMATE]_

    The what?

[CELLMATE]_

    That's |OFFICER_SURNAME| outside. They call him the Book.
    He's a total loony.

    Good luck on the outside.

Ray enters
----------

[OFFICER]_

    Prisoner |INMATE_SURNAME| step forward. Prisoner |CELLMATE_SURNAME| step forward.

[CELLMATE]_

    What, me too |OFFICER_TITLE| |OFFICER_SURNAME| ?

[OFFICER]_

    You too, |CELLMATE_SURNAME|. You will vacate this cell immediately. You will
    touch nothing on your way out.

[CELLMATE]_

    But I haven't done anything, |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    This cell is scheduled for a contraband search.

The prisoners leave
-------------------

[CELLMATE]_

    Yes, |OFFICER_TITLE| |OFFICER_SURNAME|.

[NARRATOR]_

    |CELLMATE_SURNAME| and |INMATE_SURNAME| step out of the cell onto the narrow
    balcony.

Ray joins them on the balcony
-----------------------------

[OFFICER]_

    Right, now we will proceed to the |OBJECTIVE_LABEL|.

    At the double, and in silence!

.. memory:: 197801160805
   :subject: NARRATOR

   |INMATE_FIRSTNAME| |INMATE_SURNAME| gets out of Prison today.

.. property:: NARRATOR.state 197801160805
.. property:: OFFICER.state bluemonday78.types.Spot.w12_ducane_prison_release
.. property:: INMATE.state bluemonday78.types.Spot.w12_ducane_prison_release
.. property:: CELLMATE.state bluemonday78.types.Spot.w12_ducane_prison_visiting

.. |OBJECTIVE_LABEL| property:: OBJECTIVE.label
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |INMATE_TITLE| property:: INMATE.name.title
.. |INMATE_FIRSTNAME| property:: INMATE.name.firstname
.. |INMATE_SURNAME| property:: INMATE.name.surname
