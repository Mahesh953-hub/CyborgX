import os
from userbot import Cyborg
from ..funcs.logger import logging
from ..funcs.managers import eor
from multiutility import EmojiCreator

LOGS = logging.getLogger(os.path.basename(__name__))
plugin_category = "tools"
Emoji = EmojiCreator()

@Cyborg.on_cmd(
    pattern="randomoji",
    command=("randommoji", plugin_category),
    info={
        "header": "get random emoji in image format",
        "usage": ["{tr}randomoji"],
        "examples": ["{tr}randomoji"],
    },
)
async def _(event):
    mmmm = await eor(event, "**Generating Your Random Emoji ⏰✍️**")
    emoji = Emoji.get_random()
    await event.respond("**--- Random Emoji For You ---**", file=emoji)
    os.remove(emoji)
    await mmmm.delete()
