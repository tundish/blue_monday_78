..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-04

.. |HERO| property:: HERO.name.firstname
.. |WIFE| property:: WIFE.name.firstname
.. |HUSBAND| property:: HUSBAND.name.firstname

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: bluemonday78.logic.Spot.w12_ducane_prison_visiting

   A Prison Officer. We first meet him on the day he retires.

    * Focused and conscientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: WIFE
   :types: bluemonday78.logic.PrisonVisitor

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


Stairwell
~~~~~~~~~

HM Prison Wormwood Scrubs.


Ray does the intros
-------------------


[OFFICER]_

    OK, there's no one else here. Looks like they've left me to supervise you on my
    own.

    |WIFE_TITLE| |WIFE_SURNAME|, you and |HUSBAND_FIRSTNAME| have a longer visit today
    while we're conducting an inspection of the cell.

    |HERO_TITLE| |HERO_SURNAME|, I'm going to ask you into the Guards' Office in a moment.
    Please wait right here while I open up.


[WIFE]_

    Oooh, we can choose our own table today!

[HUSBAND]_

    No, let's sit here again.


In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen talks of the journey
--------------------------


[WIFE]_

    I don't like visiting time so early. There's traffic now on the M2.

[HUSBAND]_

    Yeah.

[WIFE]_

    But it's not so bad later on.

[HUSBAND]_

    No.

[WIFE]_

    Mid morning's okay. I sometimes go with the girls for lunch at Farthing Corner.

    Which is nice.

[HUSBAND]_

    Oh.

[WIFE]_

    I really don't know why they had to move you up here. Standford Hill was much
    easier.

[HUSBAND]_

    Yeah, easier, but...

[WIFE]_

    And this place is full of hard nuts. Why did they think you belonged here? You were
    close to coming out, too.

[HUSBAND]_

    No, it's...

    A shame.

Karen talks of her work
-----------------------


[WIFE]_

    Mandy left finally, and we had a move round.
    So I've got the chair by the window now.

[HUSBAND]_

    Yeah.

[WIFE]_

    Which I like, but in the summer you get the sun right on you.

    When the drier's on that's too much.

[HUSBAND]_

    Yeah.

[WIFE]_

    And wintertime the cold comes straight through the glass.

    So for that I have my cardie.

[HUSBAND]_

    Oh.

[WIFE]_

    And you get the wind through the door.

[HUSBAND]_

    Yep.

[WIFE]_

    And I keep my bag in the back and it's further away now and I can't see it from
    where I am.

[HUSBAND]_

    No.


[WIFE]_

    But I do like it.

    Mandy had it all the time she was there so fair's fair.


[HUSBAND]_

    . . .

    So now you're working at the fair?


[WIFE]_

    No, |HUSBAND| I work at Sandy Hair.

    Next to the fair.

[HUSBAND]_

    I thought you said you worked at the fair.

    Did you get sacked from the cleaning?

[WIFE]_

    No, I still do the cleaning.

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

    See over there? |HERO|'s a friend. Gets out today.
    |HERO| will have them.

    Then you can shut up.

[WIFE]_

    Well then |HERO| can have them.
    And |HERO| had better not turn up at my door, either.
    I don't want any more of your prison mates hanging around.

[HUSBAND]_

    Hey, |HERO| do me a favour until I get out.

    The big one is for the front doors, obviously.
    The silver one is the office key.
    And this opens the padlock on the cage.

    Whatever's in the cage, you can have. But don't touch nothing else.
    Nothing else. You got that?

[HUSBAND]_

    If you see any faces sniffing around there, just tell 'em you're
    looking after it for Frankie Marshall.

    They'll get the idea.


Guards' Office
~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Ray complains about the service
-------------------------------


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

.. property:: OFFICER.state bluemonday78.logic.Spot.w12_ducane_prison_release
.. property:: HERO.state bluemonday78.logic.Spot.w12_ducane_prison_release

.. |HUSBAND_FIRSTNAME| property:: HUSBAND.name.firstname
.. |HUSBAND_SURNAME| property:: HUSBAND.name.surname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |WIFE_TITLE| property:: WIFE.name.title
.. |WIFE_SURNAME| property:: WIFE.name.surname
