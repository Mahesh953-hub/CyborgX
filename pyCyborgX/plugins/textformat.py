from . import Cyborg
from ..funcs.managers import edit_delete, eor

plugin_category = "tools"


@Cyborg.on_cmd(
    pattern=r"upper(?: |$)([\s\S]*)",
    command=("upper", plugin_category),
    info={
        "header": "Text operation change to upper text",
        "usage": "{tr}upper <input text /reply to text>",
        "examples": "{tr}upper Reply to valid text or give valid text as input",
    },
)
async def some(event):
    """Text Format upper"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.upper()
    await eor(event, mystring)


@Cyborg.on_cmd(
    pattern=r"lower(?: |$)([\s\S]*)",
    command=("lower", plugin_category),
    info={
        "header": "Text operation change to lower text",
        "usage": "{tr}lower <input text /reply to text>",
        "examples": "{tr}lower Reply to valid text or give valid text as input",
    },
)
async def good(event):
    """Text Format lower"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.lower()
    await eor(event, mystring)


@Cyborg.on_cmd(
    pattern=r"title(?: |$)([\s\S]*)",
    command=("title", plugin_category),
    info={
        "header": "Text operation change to title text",
        "usage": "{tr}title<input text /reply to text>",
        "examples": "{tr}title Reply to valid text or give valid text as input",
    },
)
async def stuff(event):
    """Text Format title"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.title()
    await eor(event, mystring)


@Cyborg.on_cmd(
    pattern=r"(|r)camel(?: |$)([\s\S]*)",
    command=("camel", plugin_category),
    info={
        "header": "Text operation change to camel text",
        "usage": [
            "{tr}camel <input text /reply to text>",
            "{tr}rcamel <input text /reply to text>",
        ],
        "examples": [
            "{tr}camel Reply to valid text or give valid text as input",
            "{tr}rcamel Reply to valid text or give valid text as input",
        ],
    },
)
async def here(event):
    """Text Format camel"""
    cmd = event.pattern_match.group(1).lower()
    intxt = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    if cmd == "r":
        bad = list(intxt.lower())[::2]
        cyborg = list(intxt.upper())[1::2]
    else:
        bad = list(intxt.upper())[::2]
        cyborg = list(intxt.lower())[1::2]
    mystring = "".join(f"{i}{j}" for i, j in zip(bad, cyborg))
    await eor(event, mystring)
