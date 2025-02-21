from pyCyborgX import Cyborg
from ..funcs.managers import eor
from ..helpers import fonts as emojify

plugin_category = "fun"


@Cyborg.on_cmd(
    pattern=r"emoji(?:\s|$)([\s\S]*)",
    command=("emoji", plugin_category),
    info={
        "header": "Converts your text to big emoji text, with some default emojis.\n use @ symbol for line space",
        "usage": "{tr}emoji <text>",
        "examples": ["{tr}emoji CyborgX"],
    },
)
async def itachi(event):
    "To get emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        await eor(
            event, "`What am I Supposed to do with this idiot, Give me a text. `"
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await eor(event, result)


@Cyborg.on_cmd(
    pattern=r"cmoji(?:\s|$)([\s\S]*)",
    command=("cmoji", plugin_category),
    info={
        "header": "Converts your text to big emoji text, with your custom emoji.\n use @ symbol for line space.",
        "usage": "{tr}cmoji <emoji> <text>",
        "examples": ["{tr}cmoji 😺 CyborgX"],
    },
)
async def itachi(event):
    "To get custom emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        return await eor(
            event, "`What am I Supposed to do with this idiot, Give me a text. `"
        )
    emoji, arg = args.split(" ", 1)
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await eor(event, result)
