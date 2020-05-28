..  Titling
    ##++::==~~--''``

.. This is a reStructuredText file.

Change Log
::::::::::

0.8.0
=====

Rolls up some minor changes in time for NarraScope 2020.

0.7.0
=====

This release establishes a structure for the dialogue which will support
an MVP release.

* Switch from explicit typing of characters to assigning a triple of traits
* Eliminate association relationships in favour of simple state changes
* Create a design document (UML activity diagram)
* Create unit tests which enforce the design

0.6.0
=====

* Add an `assembly` endpoint for JSON output of an ensemble
* Permit a `url` parameter on the POST for a new story
* Add a client to retrieve assembly JSON from a remote host
* Upgrade to `turberfield-dialogue>=0.22.0`
* Load a new story ensemble from assembly JSON
* Add a configuration file option to enable assembly features
* Implement config reload on HUP signal
* Better error handling and logging

0.5.0
=====

This release focuses on styling. Notably:

* Simplify page layout to resemble an album-cover
* Focus on two key fonts and serve them locally
* Organise CSS base variable definitions so they can be defined from code
* A first experiment with images for mood

0.4.0
=====

This release captures some of the learnings from my `PyWeek 28 entry`.

* Migrate to a Web interface
* Organise dialogue folders within directories according to location.
* Share folders across directories using symlinks.
* Programmatically create metadata to enable fast matching of dialogue
* Instant travel via a map
* Clearer organisation of story and state
* Use Memory declarations to summarise story progress

0.3.0
=====

* Basic tkinter GUI
* Full episode of dialogue

.. _PyWeek 28 entry: https://pyweek.org/e/prorogue/

