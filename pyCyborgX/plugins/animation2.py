import asyncio
from collections import deque
from . import eor, Cyborg
plugin_category = "fun"


@Cyborg.on_cmd(
    pattern="think$",
    command=("think", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}think",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="lmao$",
    command=("lmao", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}lmao",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "lmao")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="nothappy$",
    command=("nothappy", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}nothappy",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "nathappy")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="clock$",
    command=("clock", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}clock",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="muah$",
    command=("muah", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}muah",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="heart$",
    command=("heart", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}heart",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="gym$",
    command=("gym", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}gym",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="earth$",
    command=("earth", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}earth",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="moon$",
    command=("moon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}moon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="smoon$",
    command=("smoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}smoon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "smoon")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.eor("smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 8])


@Cyborg.on_cmd(
    pattern="tmoon$",
    command=("tmoon", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}tmoon",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "tmoon")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.eor("tmoon..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 32])
