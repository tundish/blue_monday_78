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
            2

.. entity:: HUSBAND
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Look.mug
            bluemonday78.types.Spot.w12_ducane_prison_visiting

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief

In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen remembers the keys
------------------------


[WIFE]_

    Which reminds me. What are all these keys for?


[HUSBAND]_

    Don't know.

    But don't wave them around.

[WIFE]_

    They came in the post the other day.

    With some documents. They were addressed to you.

    Keys to where?

[HUSBAND]_

    How would I know?

Karen is suspicious
-------------------


[WIFE]_

    So you're buying property now, |HUSBAND|?

    In your spare time.

    While you're banged up for theft.

[HUSBAND]_

    No.

Karen points the finger
-----------------------

[WIFE]_

    You're in prison and you can't read, |HUSBAND|.

    The only money we have is what I earn.

[WIFE]_

    It says, 'further to your instructions'.

[HUSBAND]_

    I'm just doing a favour for someone.

.. property:: WIFE.state 3

.. memory::  bluemonday78.types.Spot.w12_ducane_prison_visiting
   :subject: NARRATOR

   |WIFE| has intercepted a mysterious parcel.
