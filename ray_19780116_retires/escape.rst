..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-15

.. entity:: OFFICER
   :types: logic.PrisonOfficer
   :states: logic.Spot.w12_ducane_prison

.. entity:: HERO
   :types: logic.Player

   The player entity.

.. entity:: MARTIN
   :types: logic.Prisoner

   Mentioned.

Getting Out
~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray's first hint
----------------


[OFFICER]_

    I can see you have a difficult family background. Very easy to find yourself in prison
    the first time.

    If you can't get rid of the family skeleton, you may as well make it dance.

    But I'd like to say, I've been impressed by your influence on |MARTIN_FIRSTNAME| |MARTIN_SURNAME|.
    His literacy is very much improved. And he's been practicing his handwriting too, I understand.

    Well done for making it so far.

    Take every opportunity you find out there.


.. This scene should pass on a phrase for use later.

.. |HERO| property:: HERO.name.firstname
.. |MARTIN_FIRSTNAME| property:: MARTIN.name.firstname
.. |MARTIN_SURNAME| property:: MARTIN.name.surname

