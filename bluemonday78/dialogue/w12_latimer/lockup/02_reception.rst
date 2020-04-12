..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-23

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_latimer_arches

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Fit.guardian

.. entity:: HERO
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Fit.thief
            bluemonday78.types.Spot.w12_latimer_arches

A chance encounter
~~~~~~~~~~~~~~~~~~

Morning outside the warehouse.

On the approach
---------------

.. property:: OFFICER.state bluemonday78.types.Spot.w12_latimer_arches

[NARRATOR]_

    The rain has been falling since dawn.
    |HERO_FIRSTNAME| |HERO_SURNAME| peers out from the lockup.

    In a curve which follows the arches themselves, a motley array
    of vehicles is parked all the way down the lane which leads
    to the breaker's yard at the end.

[NARRATOR]_

    A solitary figure is at work. In no hurry, he is making his
    way along the line of cars. He stops at each one to peer inside.

[NARRATOR]_

    He turns away from the weather and reaches inside his coat to
    something concealed inside.

    Is he making notes?

    He has a peaked cap.

[OFFICER]_

    Well, well, well.

[HERO]_

    |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Did you know there are middle aged men on the platform at
    Latimer Road station this morning writing down the numbers of the
    trains?

[NARRATOR]_

    |OFFICER_FIRSTNAME| comes closer. He is wearing the uniform of a
    special constable.

[HERO]_

    I thought you said you'd retired,
    |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Trains are pretty boring though. They follow the same old routes
    and you know exactly when to catch them.

    Not so with cars. They pop up in all sorts of strange places.

[OFFICER]_

    My colleagues don't understand why I volunteer for this duty.
    But it's very often the way in to some very significant
    discoveries.

[NARRATOR]_

    |OFFICER_FIRSTNAME| smiles. For rather too long.

[OFFICER]_

    You fell on your feet, didn't you? At some point soon we are
    going to have a little chat about your new employers.

[HERO]_

    This place belongs to Frankie Marshall.

[NARRATOR]_

    |OFFICER_FIRSTNAME| stops smiling.
 
[OFFICER]_

    And I'd say that's where your problems begin.

.. property:: OFFICER.state 19780119

.. Needs alternative for "show yourself":
.. I'm going to put you straight.
.. Insubordinate. Insolent. A trickster with criminal tendencies.
.. That last quality might be useful.
.. But if I have any trouble with you |HERO|,  I shall bite you, |HERO|.
.. And I shall bite you so hard you'll go right back to where I found you.


.. |HERO_FIRSTNAME| property:: HERO.name.firstname
.. |HERO_SURNAME| property:: HERO.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
