..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |HERO| property:: HERO.name.firstname

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

Ray complains about the service
-------------------------------

[NARRATOR]_

    The Guard's Room is a shabby little office. There are some filing cabinets and a couple
    of chairs. Everything is painted a thick institutional green.

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| is tidying up a high wooden desk.

[OFFICER]_

    Dear oh dear, what a mess today. I'm the only one who tidies this place up.

    No-one replaces the stationery here you know. I had to bring in a load of rubber bands
    this morning from home.

    The only thing we've got left here is pens. Shamefully no one seems to want to steal
    those.

Ray does the paperwork
----------------------

.. This shot has to end in a question. It invites user input.

[OFFICER]_

    Well, now, let's have you on your way.


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
