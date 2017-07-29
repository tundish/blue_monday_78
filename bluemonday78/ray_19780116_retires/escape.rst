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

    It's a funny thing. This happens to be my last day as well.
    I'm about to take early retirement.

    After thirty years. I came straight out of the Army into the Prison Service.

    So at least we have this in common; neither of us can wait to get out of here! 

.. Martin and Karen's argument has become very loud.

[OFFICER]_

    There's never enough time is there, to say what we have to. But I'd like
    you to know I've been impressed by your influence on |MARTIN_FIRSTNAME| |MARTIN_SURNAME|.
    His literacy is very much improved. And he's been practicing his handwriting too, I understand.

.. There is cursing and screaming.

[OFFICER]_

    And I know why that is. You didn't start out with many options in life.
    We know you have a difficult family background.

    Most people don't recover from such a beginning. Except, you have a very special
    kind of tenacity. You don't give up, do you?

    I'd just like you to know, that I admire your attitude. Although I can see it might
    lead to more trouble if you're not careful.

.. An alarm bell rings.

[OFFICER]_

    So just let me say this.

    If you can't get rid of the family skeleton, you may as well make it dance, eh?

    Now, goodbye, and good luck.

.. This scene should pass on a phrase for use later.

.. |HERO| property:: HERO.name.firstname
.. |MARTIN_FIRSTNAME| property:: MARTIN.name.firstname
.. |MARTIN_SURNAME| property:: MARTIN.name.surname

