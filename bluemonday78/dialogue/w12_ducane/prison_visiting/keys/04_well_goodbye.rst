..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: bluemonday78.story.version

.. TODO: Rename this file

:author: D Haynes
:date: 2017-07-04
:project: bluemonday78
:version: |VERSION|

.. |INMATE| property:: INMATE.nickname
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

Do me a favour
--------------

[WIFE]_

    What are you doing?

[HUSBAND]_

    Look, it's just a favour for somebody.

[WIFE]_

    A favour? In here? I bet.

    Someone's put one on you.
    I knew this would happen as soon as you got up here.

[HUSBAND]_

    It's not like that.

Karen has seen it all before
----------------------------

[WIFE]_

    Every time.

    You fall for every dodgy scheme.

[HUSBAND]_

    It's just a little bit of business.

    Stay out of it.

[WIFE]_

    And it's not you that suffers in the end, it's me and the kids.
    It always comes back on us!

Getting shouty
--------------

[HUSBAND]_

    Keep your voice down, or the screw will come over.

[WIFE]_

    Or maybe I should call him over.

    You're not doing this to us again.

    I'm sick of bloody solicitors and loan agreements and ...

    Bailiffs! 

Kicking off
-----------

[HUSBAND]_

    All right. Shut up.

[WIFE]_

    Don't you...

[HUSBAND]_

    Shut up, will you.

[WIFE]_

    Don't you ever...

[HUSBAND]_

    |INMATE| has got them.

    So now you can shut up.

.. property:: WIFE.state 4
