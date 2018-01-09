..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. entity:: NARRATOR
   :types: bluemonday78.logic.Narrator

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: bluemonday78.logic.Spot.w12_ducane_prison_visiting

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: CELLMATE
   :types: bluemonday78.logic.Prisoner

   A small-time offender in his mid forties.

.. entity:: HERO
   :types: bluemonday78.logic.Player

   The player entity.

A Prison Wing
~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.


Ray is at the door
------------------

[NARRATOR]_

    We fade in to the sound of keys in an iron door.

[CELLMATE]_

    Good luck then, |HERO_FIRSTNAME| mate. Stay lucky.

    I wonder who they're going to put in here with me next?

[OFFICER]_

    Prisoner |HERO_SURNAME| step forward. Prisoner |CELLMATE_SURNAME| step forward.

[CELLMATE]_

    What, me too |OFFICER_TITLE| |OFFICER_SURNAME| ?

[OFFICER]_

    You too, |CELLMATE_SURNAME|. You will vacate this cell immediately. You will
    touch nothing on your way out.

[CELLMATE]_

    Yes, |OFFICER_TITLE| |OFFICER_SURNAME|.

.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
