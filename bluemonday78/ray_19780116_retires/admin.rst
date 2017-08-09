..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-04

.. |HERO| property:: HERO.name.firstname
.. |KAREN| property:: KAREN.name.firstname
.. |MARTIN| property:: MARTIN.name.firstname

.. entity:: OFFICER
   :types: bluemonday78.logic.PrisonOfficer
   :states: bluemonday78.logic.Spot.w12_ducane_prison

   A Prison Officer. We first meet him on the day he retires.

    * Focussed and concientious
    * Bruised by too many years in the service
    * Often upset by inefficiency and lack of structure

.. entity:: KAREN
   :types: bluemonday78.logic.PrisonVisitor

   A beautician in her late forties.

    * Works in `Sandy Hair`, Leysdown-on-Sea.
    * Very organised.
    * Has always looked after |MARTIN|.

.. entity:: MARTIN
   :types: bluemonday78.logic.Prisoner

   A small-time offender in his mid forties.

    * Can't read. Dislocated.
    * Does what he's told. Wants a quiet life.
    * Misbehaved at Standford Hill to see less of |KAREN|.

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

    |KAREN_TITLE| |KAREN_SURNAME|, you and |MARTIN_FIRSTNAME| have a longer visit today
    while we're conducting an inspection of the cell.

    |HERO_TITLE| |HERO_SURNAME|, I'm going to ask you into the Guard's Office in a moment.
    Please wait right here while I open up.


[KAREN]_

    Oooh, we can choose our own table today!

[MARTIN]_

    No, let's sit here again.


In the Visiting Suite
~~~~~~~~~~~~~~~~~~~~~

HM Prison Wormwood Scrubs.

Karen talks of the journey
--------------------------


[KAREN]_

    I don't like visiting time so early. There's traffic now on the M2.

[MARTIN]_

    Yeah.

[KAREN]_

    But it's not so bad later on.

[MARTIN]_

    No.

[KAREN]_

    Mid morning's okay. I sometimes go with the girls for lunch at Farthing Corner.

    Which is nice.

[MARTIN]_

    Oh.

[KAREN]_

    I really don't know why they had to move you up here. Standford Hill was much
    easier.

[MARTIN]_

    Yeah, easier, but...

[KAREN]_

    And this place is full of hard nuts. Why did they think you belonged here? You were
    close to coming out, too.

[MARTIN]_

    No, it's...

    A shame.

Karen talks of her work
-----------------------


[KAREN]_

    Mandy left finally, and we had a move round.
    So I've got the chair by the window now.

[MARTIN]_

    Yeah.

[KAREN]_

    Which I like, but in the summer you get the sun right on you.

    When the drier's on that's too much.

[MARTIN]_

    Yeah.

[KAREN]_

    And wintertime the cold comes straight through the glass.

    So for that I have my cardie.

[MARTIN]_

    Oh.

[KAREN]_

    And you get the wind through the door.

[MARTIN]_

    Yep.

[KAREN]_

    And I keep my bag in the back and it's further away now and I can't see it from
    where I am.

[MARTIN]_

    No.


[KAREN]_

    But I do like it.

    Mandy had it all the time she was there so fair's fair.


[MARTIN]_

    . . .

    So now you're working at the fair?


[KAREN]_

    No, |MARTIN| I work at Sandy Hair.

    Next to the fair.

[MARTIN]_

    I thought you said you worked at the fair.

    Did you get sacked from the cleaning?

[KAREN]_

    No, I still do the cleaning.

Karen talks of the keys
-----------------------


[KAREN]_

    Which reminds me. What are these for?


[MARTIN]_

    What?

    Don't know.

    But don't wave them around.

[KAREN]_

    They came in the post the other day.

    With some documents. They were addressed to you.

    This is a property deed, in't it?

[MARTIN]_

    How would I know?

[KAREN]_

    Do you own property now, |MARTIN|? While you're banged up for theft
    and the only money we have is what I earn?

[MARTIN]_

    I'm just doing a favour for someone.

[KAREN]_

    A favour? Lord, what are you mixed up in now? A favour.

    Someone's put one on you. You're getting letters from law firms and
    you can't even read.

    Every chance that comes along you go and fall for some dodgy deal.
    And it's not you that suffers in the end, it's me and the kids.
    It always comes back on us!

[MARTIN]_

    Keep your voice down, or the screw will come over.

[KAREN]_

    Or maybe I should call him over. You're not doing this to us again.
    I'm sick of bloody solicitors and loan agreements and ...

    Bailiffs! 

[MARTIN]_

    All right. Shut up.

    Shut up, will you.

    See over there? That's my cellie. Gets out today.
    |HERO| will have them.

    Then you can shut up.

[KAREN]_

    Well |HERO| can have them. And |HERO| had better not turn up at my door, either.
    I don't want any more of your prison mates hanging around.

[MARTIN]_

    Hey, |HERO| do me a favour until I get out.

    The big one is for the front doors. Silver one is the office key.
    And this one opens the padlock on the cage.

    Whatever's in the cage, you can have. Don't touch nothing else. You got that?

[MARTIN]_

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

.. This shot should end in a question. The next interlude will be the first to need user input/

[OFFICER]_

    Well, now, let's have you on your way.


[OFFICER]_

    It isn't usual to read a form B107 to its subject, |HERO_TITLE| |HERO_SURNAME|, but
    it looks like you've been playing it straight.

.. property:: OFFICER.state bluemonday78.logic.Spot.w12_ducane_prison_release

.. |MARTIN_FIRSTNAME| property:: MARTIN.name.firstname
.. |MARTIN_SURNAME| property:: MARTIN.name.surname
.. |HERO_TITLE| property:: HERO.name.title
.. |HERO_SURNAME| property:: HERO.name.surname
.. |KAREN_TITLE| property:: KAREN.name.title
.. |KAREN_SURNAME| property:: KAREN.name.surname
