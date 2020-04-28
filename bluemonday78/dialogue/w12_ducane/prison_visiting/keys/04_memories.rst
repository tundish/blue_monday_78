..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

.. TODO: Rename this file

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |INMATE| property:: INMATE.name.firstname
.. |WIFE| property:: WIFE.name.firstname
.. |HUSBAND| property:: HUSBAND.name.firstname

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: WIFE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.healer
            bluemonday78.types.Spot.w12_ducane_prison_visiting
            3

.. entity:: HUSBAND
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief
            bluemonday78.types.Spot.w12_ducane_prison_release

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

    See over there? |INMATE| was in my cell. Gets out today.
    |INMATE| will take them for a while.

    Then you can shut up.

[WIFE]_

    Well then |INMATE| can have them.
    And |INMATE| had better not turn up at my door, either.
    I don't want any more of your prison mates hanging around.

.. property:: WIFE.state 2

