..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.logic.version

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |HERO| property:: HERO.name.firstname
.. |WIFE| property:: WIFE.name.firstname
.. |HUSBAND| property:: HUSBAND.name.firstname

.. entity:: WIFE
   :types: bluemonday78.logic.PrisonVisitor
   :states: 197801160820

   A beautician in her late forties.

    * Works in `Sandy Hair`, Leysdown-on-Sea.
    * Very organised.
    * Has always looked after |HUSBAND|.

.. entity:: HUSBAND
   :types: bluemonday78.logic.Prisoner

   A small-time offender in his mid forties.

    * Can't read. Dislocated.
    * Does what he's told. Wants a quiet life.
    * Misbehaved at Standford Hill to see less of |WIFE|.

.. entity:: HERO
   :types: bluemonday78.logic.Player

   The player entity.

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen talks of the keys
-----------------------


[WIFE]_

    Which reminds me. What are these for?


[HUSBAND]_

    What?

    Don't know.

    But don't wave them around.

[WIFE]_

    They came in the post the other day.

    With some documents. They were addressed to you.

    This is a property deed, isn't it?

[HUSBAND]_

    How would I know?

[WIFE]_

    So you own property now, |HUSBAND|? While you're banged up for theft
    and the only money we have is what I earn?

[HUSBAND]_

    No.

[WIFE]_

    It says, 'further to your instructions'. But you can't even read, |HUSBAND|.

[HUSBAND]_

    I'm just doing a favour for someone.

[WIFE]_

    A favour? Lord, what are you mixed up in now? A favour.

    Someone's put one on you.
    I knew this would happen as soon as you got up here.

    Every chance that comes along you go and fall for some dodgy scam.
    And it's not you that suffers in the end, it's me and the kids.
    It always comes back on us!

[HUSBAND]_

    Keep your voice down, or the screw will come over.

[WIFE]_

    Or maybe I should call him over. You're not doing this to us again.
    I'm sick of bloody solicitors and loan agreements and ...

    Bailiffs! 

[HUSBAND]_

    All right. Shut up.

    Shut up, will you.

    See over there? |HERO| was in my cell. Gets out today.
    |HERO| will take them for a while.

    Then you can shut up.

[WIFE]_

    Well then |HERO| can have them.
    And |HERO| had better not turn up at my door, either.
    I don't want any more of your prison mates hanging around.

.. property:: WIFE.state 197801160830
