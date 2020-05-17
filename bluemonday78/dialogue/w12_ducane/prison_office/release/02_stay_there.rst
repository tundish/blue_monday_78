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
   :states: bluemonday78.types.Spot.w12_ducane_prison_release
            197801160805

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.guardian
            bluemonday78.types.Spot.w12_ducane_prison_release

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief
            bluemonday78.types.Spot.w12_ducane_prison_wing

.. entity:: CELLMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.mug
            bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: OBJECTIVE
   :types:  bluemonday78.types.Location
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting


Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray unlocks the office
----------------------

[OFFICER]_

    |INMATE_SURNAME| you stay here while I unlock the Office.

[OFFICER]_

    I'll be back in five minutes.

    There'll be no nonsense while my back is turned, |INMATE_SURNAME|.

.. memory:: 197801160810
   :subject: NARRATOR

   |OFFICER_SURNAME| is distracted.

.. property:: INMATE.state bluemonday78.types.Spot.w12_ducane_prison_visiting

.. |CELLMATE_FIRSTNAME| property:: CELLMATE.name.firstname
.. |CELLMATE_SURNAME| property:: CELLMATE.name.surname
.. |INMATE_NICK| property:: INMATE.nickname
.. |INMATE_FIRSTNAME| property:: INMATE.name.firstname
.. |INMATE_SURNAME| property:: INMATE.name.surname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
