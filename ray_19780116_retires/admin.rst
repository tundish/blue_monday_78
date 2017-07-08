..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-04

.. |HERO| property:: HERO.name.firstname
.. |KAREN| property:: KAREN.name.firstname
.. |MARTIN| property:: MARTIN.name.firstname

.. entity:: OFFICER
   :types: logic.PrisonOfficer
   :states: logic.Spot.w12_ducane_prison

   A Prison Officer. We first meet him on the day he retires.

    * Focussed and concientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: KAREN
   :types: logic.PrisonVisitor

   A beautician in her late forties.

    * Works in `Sandy Hair`, Leysdown-on-Sea.
    * Very organised.
    * Has always looked after |MARTIN|.

.. entity:: MARTIN
   :types: logic.Prisoner

   A small-time offender in his mid forties.

    * Can't read. Dislocated.
    * Does what he's told. Wants a quiet life.
    * Misbehaved at Standford Hill to see less of |KAREN|.

.. entity:: HERO
   :types: logic.Player

   The player entity.


First positions
~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs, J Wing.


Ray does the intros
-------------------


[OFFICER]_

    OK, there's no one else here. Looks like they've left me to supervise you on my
    own.

    |KAREN_TITLE| |KAREN_SURNAME|, you and |MARTIN_FIRSTNAME| have a longer visit today
    while we're conducting an inspection of the cell.

    |HERO_TITLE| |HERO_SURNAME|, I'm going to ask you into the Guard's Office in a moment.
    Please wait right here while I open up.


[KAREN]_

    Oooh, we can choose our own table today!

[MARTIN]_

    No, let's sit here again.

.. |MARTIN_FIRSTNAME| property:: MARTIN.name.firstname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |KAREN_TITLE| property:: KAREN.name.title
.. |KAREN_SURNAME| property:: KAREN.name.surname
