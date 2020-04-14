..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

:author: D Haynes
:date: 2018-02-14
:project: bluemonday78
:version: |VERSION|

.. |HERO| property:: HERO.name.firstname

.. entity:: NARRATOR
   :types: bluemonday78.types.Narrator

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Fitt.guardian
            bluemonday78.types.Spot.w12_ducane_prison_release

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: HERO
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Fitt.thief
            bluemonday78.types.Spot.w12_ducane_prison_release

   The player entity.


Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray bestows a parting gift
--------------------------

[NARRATOR]_

    The Guard's Room is a shabby little office. There are some filing cabinets and a couple
    of chairs. Everything is painted a thick institutional green.

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| is rearranging boxes on a high wooden desk.

[OFFICER]_

    Good Lord, what a mess. I'm the only one who tidies this place up.

    No-one replaces the stationery here you know. I had to bring in a load of rubber bands
    this morning from home. And I see we're out of pens again.

[NARRATOR]_

    |OFFICER_FIRSTNAME| |OFFICER_SURNAME| pulls something out of a box near the floor.
    He looks at it for a moment.

[OFFICER]_

    You may as well have this. It's not doing any good in here.

[NARRATOR]_

    |OFFICER_SURNAME| tosses onto the desk a small book. Its cover is of stiffened cloth.
    A few dozen waxy leaves of thick paper have been double-punched through with holes.
    It is held together by a shoelace.

Ray shares a memory
-------------------

[OFFICER]_

    I would always issue these to my squad leaders. I used to train them
    to make a note of everything they saw.

[HERO]_

    Thanks, |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Can't give you a pen I'm afraid.

[HERO]_

    That's okay, |OFFICER_TITLE| |OFFICER_SURNAME|.

[NARRATOR]_

    Someone has been throwing sharpened pencils at the suspended ceiling. Two or
    three are stuck into the soft board and are just within reach.

[OFFICER]_

    Help yourself to a pencil, though.

[OFFICER]_

    It isn't usual to read a form B107 to its subject,
    |HERO_TITLE| |HERO_SURNAME|, but it looks like you've been playing it
    straight.

    That's what we like to see, eh?

.. property:: OFFICER.state 197801160810

.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
