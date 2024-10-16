import nekos
from pyCyborgX import Cyborg
from ..funcs.managers import eor

plugin_category = "fun"


@Cyborg.on_cmd(
    pattern="tlion$",
    command=("tlion", plugin_category),
    info={
        "header": "Some random lion facial text art",
        "usage": "{tr}tlion",
    },
)
async def hmm(lion):
    "Some random lion facial text art"
    reactlion = nekos.textlion()
    await eor(lion, reactlion)


@Cyborg.on_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(cyborg):
    "Some random Funny questions"
    nekos.why()
    await eor(cyborg, whycat)


@Cyborg.on_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(cyborg):
    "Some random facts"
    factcyborg = nekos.fact()
    await eor(cyborg, factcyborg)
