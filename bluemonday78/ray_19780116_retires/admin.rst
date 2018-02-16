..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: bluemonday78.logic.Spot.w12_ducane_prison_release
            197801160810

.. entity:: HERO
   :types: bluemonday78.logic.Player
   :states: bluemonday78.logic.Spot.w12_ducane_prison_release

.. entity:: NARRATOR
   :types: bluemonday78.logic.Narrator

Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray does the paperwork
----------------------

.. This shot has to end in a question. It invites user input.

[OFFICER]_

    Don't think for a second I want you hanging around here, |HERO_SURNAME|.


[OFFICER]_

    It isn't usual to read a form B107 to its subject,
    |HERO_TITLE| |HERO_SURNAME|, but it looks like you've been playing it
    straight.

    That's what we like to see, eh?

.. property:: OFFICER.state 197801160820

.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
