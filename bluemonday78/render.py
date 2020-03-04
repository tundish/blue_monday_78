#!/usr/bin/env python3
# encoding: UTF-8

# This file is part of Addison Arches.
#
# Addison Arches is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Addison Arches is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Addison Arches.  If not, see <http://www.gnu.org/licenses/>.

import functools
from turberfield.dialogue.model import Model

from bluemonday78.presenter import Presenter
from bluemonday78.matcher import MultiMatcher
from bluemonday78.types import Location
from bluemonday78.types import Persona
from bluemonday78.types import Player
from bluemonday78.types import Spot
from bluemonday78.types import Page

"""
http://css3.bradshawenterprises.com/cfimg/
For "n" images You must define:
a=presentation time for one image
b=duration for cross fading
Total animation-duration is of course t=(a+b)*n

animation-delay = t/n or = a+b

Percentage for keyframes:

    0%
    a/t*100%
    (a+b)/t*100% = 1/n*100%
    100%-(b/t*100%)
    100%
"""

def animated_line_to_html(anim):
    return f"""
<li style="animation-delay: {anim.delay:.2f}s; animation-duration: {anim.duration:.2f}s">
<blockquote class="obj-line">
<header class="{'obj-persona' if hasattr(anim.element.persona, '_name') else ''}">
{ '{0.firstname} {0.surname}'.format(anim.element.persona.name) if hasattr(anim.element.persona, 'name') else ''}
</header>
<p class="obj-speech">{ anim.element.text }</p>
</blockquote>
</li>"""


def animated_still_to_html(anim):
    return f"""
<div style="animation-duration: {anim.duration}s; animation-delay: {anim.delay}s">
<img src="/img/{anim.element.resource}" alt="{anim.element.package} {anim.element.resource}" />
</div>"""


def audio_to_html(elem):
    return f"""<div>
<audio src="/audio/{elem.resource}" autoplay="autoplay" preload="auto" >
</audio>
</div>"""


def location_to_html(locn, path="/"):
    return f"""
<form role="form" action="{path}hop" method="post" name="{locn.id.hex}" >
    <input id="hop-{locn.id.hex}" name="location_id" type="hidden" value="{locn.id.hex}" />
    <button type="submit">{locn.label}</button>
</form>"""


def ensemble_to_html(ensemble):
    player = ensemble[-1]
    spot = player.get_state(Spot)
    assert isinstance(player, Player)
    notes = "\n".join(
        "<li>{0.html}</li>".format(i)
        for i in getattr(player, "memories", [])
    )
    items = "\n".join(
        "<li>{0.label}</li>".format(i) for i in ensemble
        if not isinstance(i, (Location, Persona)) and hasattr(i, "label")
    )
    moves = "\n".join(
        "<li>{0}</li>".format(location_to_html(i, path="/{0.id.hex}/".format(player)))
        for i in ensemble
        if isinstance(i, Location) and
        i.get_state(Page) != Page.closed
    )
    return f"""
<aside class="grid-flash">
</aside>
<nav class="grid-study">
<ul class="mod-moves">
{moves}
</ul>
</nav>
<main class="grid-state">
<ul class="mod-dialogue">
{notes}
</ul>
<ul class="mod-inventory">
{items}
</ul>
</main>
<section class="grid-focus">
<dl class="mod-stats"><dt>Time</dt>
<dd>{MultiMatcher.parse_timespan(str(player.state))[0].ctime()}</dd>
</dl>
</section>"""


def frame_to_html(frame, ensemble=[], final=False):
    player = ensemble[-1] if ensemble else None
    spot = player.get_state(Spot) if player else None
    dialogue = "\n".join(animated_line_to_html(i) for i in frame[Model.Line])
    stills = "\n".join(animated_still_to_html(i) for i in frame[Model.Still])
    audio = "\n".join(audio_to_html(i) for i in frame[Model.Audio])
    return f"""
{audio}
<section class="lay-banner">
<h1><span>Blue</span><span>Monday</span><span>78</span></h1>
<h2>Pilot Episode</h2>
</section>
<aside class="lay-photos">
{stills}
</aside>
<div class="lay-speech">
<main>
{'<h1>{0}</h1>'.format(spot.value[-1].capitalize().replace("_", " ")) if spot is not None else ''}
<ul class="obj-dialogue">
{dialogue}
</ul>
</main>
<nav>
{'<a href="/{0.id.hex}/map">Go</a>'.format(player) if player and final else ''}
</nav>
</div>"""


def titles_to_html():
    return f"""
<form role="form" action="/" method="POST" name="titles" class="grid-flash mod-titles">
  <h1>Start a new story.</h1>
    <fieldset>
    <label for="player-name" id="player-name-tip">Choose a character name</label>
    <input
    name="playername"
    type="text"
    id="player-name"
    required="required"
    aria-describedby="player-name-tip"
    placeholder="?"
    pattern="{Presenter.validation["name"].pattern}"
    >
    <button type="submit">Enter</button>
    </fieldset>
    <!-- <fieldset>
    <label for="email">Email</label>
    <input
    name="email"
    id="email"
    placeholder="@"
    aria-describedby="email-tip"
    pattern="{{ validation["email"].pattern }}"
    >
    <small id="email-tip">optional</small>
    </fieldset> -->
</form>
<p>You can get the code for this story from
<a href="https://github.com/tundish/blue_monday_78">GitHub</a>.</p>"""


def vars_to_html(definitions=None):
    definitions = definitions or {}
    entries = "\n".join("--{0}: {1};".format(k, v) for k, v in definitions.items())

    return f""":root {{
{entries}
}}"""

@functools.lru_cache()
def body_html(refresh=None):
    # TODO: Add style tag for css content
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{'<meta http-equiv="refresh" content="{0}">'.format(refresh) if refresh is not None else ''}
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Blue Monday 78: Pilot episode</title>
<link rel="stylesheet" href="/css/blomt.css" />
</head>
<body>
<style type="text/css">
{{0}}
</style>
{{1}}
</body>
</html>"""
