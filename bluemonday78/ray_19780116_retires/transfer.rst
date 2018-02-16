..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. entity:: WIFE
   :types: bluemonday78.logic.PrisonVisitor
   :states: 197801160830

.. entity:: CELLMATE
   :types: bluemonday78.logic.Prisoner

.. entity:: HERO
   :types: bluemonday78.logic.Player
   :states: bluemonday78.logic.Spot.w12_ducane_prison_visiting

.. entity:: NARRATOR
   :types: bluemonday78.logic.Narrator

.. entity:: OBJECTIVE
   :types: bluemonday78.logic.Location
   :states: bluemonday78.logic.Spot.w12_latimer_arches

.. entity:: EXIT
   :types: bluemonday78.logic.Location
   :states: bluemonday78.logic.Spot.w12_ducane_prison_release

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Martin hands over the keys
--------------------------

[NARRATOR]_

    |CELLMATE| sidles over.

[CELLMATE]_

    |HERO| mate; quick. Take these keys. The address is on the
    label. Keep them out of sight.

[NARRATOR]_

    |CELLMATE| lowers his voice.

[CELLMATE]_

    It belongs to a firm over the West End. There's going to be a delivery come in soon
    and when it does, they're gonna stash it in there.

    In the cage downstairs is a load of tatty gear. You've got to clear that all
    out, or there won't be room for the new stuff.

[NARRATOR]_

    |CELLMATE| eyes |HERO| nervously.

[CELLMATE]_

    Make sure that place is empty soon, or I'm gonna get a beating!

    And don't let anybody in there. If you get anyone poking around,
    tell them you're looking after it for Frankie Marshall.

.. memory:: bluemonday78.types.Via.forwd
   :subject: EXIT
   :object: OBJECTIVE

   |OBJECTIVE_LABEL| is accessible.

.. memory:: bluemonday78.types.Travel.intention
   :subject: HERO
   :object: OBJECTIVE

   Go to |OBJECTIVE_LABEL| and empty the downstairs
   cage so it's ready when Frankie Marshall wants it.

.. |CELLMATE| property:: CELLMATE.name.firstname
.. |HERO| property:: HERO.name.firstname
.. |OBJECTIVE_LABEL| property:: OBJECTIVE.label
