from PyDictionary import PyDictionary
from pyCyborgX import Cyborg
from ..funcs.logger import logging
from ..funcs.managers import edit_delete, eor
from ..helpers import AioHttp
from ..helpers.utils import _format

LOGS = logging.getLogger(__name__)
plugin_category = "utils"


@Cyborg.on_cmd(
    pattern=r"ud ([\s\S]*)",
    command=("ud", plugin_category),
    info={
        "header": "To fetch meaning of the given word from urban dictionary.",
        "usage": "{tr}ud <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from urban dictionary."
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n`{}`\n\n**Example:**\n`{}`".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await eor(event, result)
    except Exception as e:
        await edit_delete(
            event,
            text="`The Urban Dictionary API could not be reached`",
        )
        LOGS.info(e)


@Cyborg.on_cmd(
    pattern=r"meaning ([\s\S]*)",
    command=("meaning", plugin_category),
    info={
        "header": "To fetch meaning of the given word from dictionary.",
        "usage": "{tr}meaning <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from dictionary."
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    cyborg = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in cyborg.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await eor(event, output)
    except Exception:
        await eor(event, f"Couldn't fetch meaning of {word}")
