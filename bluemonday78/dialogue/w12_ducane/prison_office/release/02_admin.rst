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
   :states: 197801160805

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Fit.guardian
            bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: HERO
   :types: bluemonday78.types.Character
   :states: bluemonday78.types.Fit.thief
            bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: CELLMATE
   :types: bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: OBJECTIVE
   :types: bluemonday78.types.Location
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray splits them up
------------------

[OFFICER]_

    |CELLMATE_SURNAME|, your lady wife has arrived outside. So you will have
    visiting time until 09:00.

[CELLMATE]_

    Yes, |OFFICER_TITLE| |OFFICER_SURNAME|.

Ray unlocks the office
----------------------

[OFFICER]_

    |HERO_SURNAME| you stay here while I unlock the Office.

[OFFICER]_

    I'll be back in five minutes.

    There'll be no nonsense while my back is turned, |HERO_SURNAME|.

.. memory:: 197801160811
   :subject: HERO

   |HERO_FIRSTNAME| |HERO_SURNAME| is waiting for |OFFICER_SURNAME| to get back.

.. property:: OBJECTIVE.state bluemonday78.types.Page.opened

.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
