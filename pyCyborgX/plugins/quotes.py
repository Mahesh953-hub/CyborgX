import random
from . import Cyborg
from ..funcs.logger import logging
from ..funcs.managers import edit_delete, eor
from ..helpers import cyborgmemes
from ..helpers.functions import random_quote, search_quotes
from ..helpers.utils import parse_pre

LOGS = logging.getLogger(__name__)
plugin_category = "tools"


@Cyborg.on_cmd(
    pattern=r"quote(?:\s|$)([\s\S]*)",
    command=("quote", plugin_category),
    info={
        "header": "To get random quotes on given topic.",
        "description": "An api that Fetchs random Quote from `goodreads.com`",
        "usage": "{tr}quote <topic>",
        "examples": "{tr}quote love",
    },
)
async def quote_search(event):
    "shows random quotes on given topic."
    input_str = event.pattern_match.group(1)
    try:
        response = await search_quotes(input_str) if input_str else await random_quote()
    except Exception:
        return await edit_delete(event, "`Sorry Zero results found`", 5)
    await eor(event, response, parse_mode=parse_pre)


@Cyborg.on_cmd(
    pattern="pquote$",
    command=("pquote", plugin_category),
    info={
        "header": "To get random quotes on programming.",
        "usage": "{tr}pquote",
    },
)
async def _(event):
    "Shows random programming quotes"
    txt = random.choice(cyborgmemes.PROGQUOTES)
    await eor(event, txt)
