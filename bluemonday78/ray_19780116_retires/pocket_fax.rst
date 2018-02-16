..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2018-02-14
:project: bluemonday78
:version: |VERSION|

.. |HERO| property:: HERO.name.firstname

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: bluemonday78.logic.Spot.w12_ducane_prison_release
            197801160800

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: HERO
   :types: bluemonday78.logic.Player
   :states: bluemonday78.logic.Spot.w12_ducane_prison_release

   The player entity.

.. entity:: NARRATOR
   :types: bluemonday78.logic.Narrator


Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray bestows a parting gift
--------------------------

[NARRATOR]_

    The Guard's Room is a shabby little office. There are some filing cabinets and a couple
    of chairs. Everything is painted a thick institutional green.

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| is tidying up a high wooden desk.

[OFFICER]_

    Good Lord, what a mess. I'm the only one who tidies this place up.

    No-one replaces the stationery here you know. I had to bring in a load of rubber bands
    this morning from home.

[NARRATOR]_

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| pulls something out of a box near the floor.
    He looks at it for a moment.

[OFFICER]_

    You may as well have this. It's not doing any good in here.

.. property:: OFFICER.state 197801160810

.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
