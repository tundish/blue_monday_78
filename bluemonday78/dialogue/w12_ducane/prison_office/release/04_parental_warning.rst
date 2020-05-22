..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

:author: D Haynes
:date: 2017-07-23

.. entity:: NARRATOR
   :types:  bluemonday78.types.Narrator
   :states: bluemonday78.types.Spot.w12_latimer_arches
            19780117

.. entity:: OFFICER
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.guardian

.. entity:: INMATE
   :types:  bluemonday78.types.Character
   :states: bluemonday78.types.Mode.thief
            bluemonday78.types.Spot.w12_latimer_arches

A chance encounter
~~~~~~~~~~~~~~~~~~

Morning outside the warehouse.

On the approach
---------------

.. property:: OFFICER.state bluemonday78.types.Spot.w12_latimer_arches

[NARRATOR]_

    The rain has been falling since dawn.
    |INMATE_FIRSTNAME| |INMATE_SURNAME| peers out from the lockup.

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

[INMATE]_

    |OFFICER_TITLE| |OFFICER_SURNAME|.

[OFFICER]_

    Did you know there are middle aged men on the platform at
    Latimer Road station this morning writing down the numbers of the
    trains?

[NARRATOR]_

    |OFFICER_FIRSTNAME| comes closer. He is wearing the uniform of a
    special constable.

[INMATE]_

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

    This your place of business is it? At some point soon we are
    going to have a little chat about your new employers.

[INMATE]_

    It belongs to Frankie Marshall.

[NARRATOR]_

    |OFFICER_FIRSTNAME| stops smiling.
 
[OFFICER]_

    Well I'd say this is where your problems begin.

.. property:: NARRATOR.state 197801170820

.. Needs alternative for "show yourself":
.. I'm going to put you straight.
.. Insubordinate. Insolent. A trickster with criminal tendencies.
.. That last quality might be useful.
.. But if I have any trouble with you |INMATE|,  I shall bite you, |INMATE|.
.. And I shall bite you so hard you'll go right back to where I found you.


.. |INMATE_FIRSTNAME| property:: INMATE.name.firstname
.. |INMATE_SURNAME| property:: INMATE.name.surname
.. |OFFICER_TITLE| property:: OFFICER.name.title
.. |OFFICER_FIRSTNAME| property:: OFFICER.name.firstname
.. |OFFICER_SURNAME| property:: OFFICER.name.surname
