import asyncio
from collections import deque
from . import edit_delete, eor, Cyborg, mention

plugin_category = "fun"

@Cyborg.on_cmd(
    pattern="star$",
    command=("star", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}star",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "`stars.....`")
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="boxs$",
    command=("boxs", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}boxs",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "`boxs...`")
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="rain$",
    command=("rain", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}rain",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "`Raining.......`")
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.eor("".join(deq))
        deq.rotate(1)


@Cyborg.on_cmd(
    pattern="deploy$",
    command=("deploy", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}deploy",
    },
)
async def _(event):
    "animation command"
    animation_interval = 3
    animation_ttl = range(12)
    event = await eor(event, "`Deploying...`")
    animation_chars = [
        "**Heroku Connecting To Latest Github Build **",
        f"**Build started by user** {mention}",
        f"**Deploy** `535a74f0` **by user** {mention}",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m userbot`",
        "**State changed from starting to up**",
        "__INFO:Userbot:Logged in as 557667062__",
        "__INFO:Userbot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 12])


@Cyborg.on_cmd(
    pattern=r"dump(?:\s|$)([\s\S]*)",
    command=("dump", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}dump <any three emoji's(optional)>",
        "examples": ["{tr}dump", "{tr}dump 🍰🍎🐓"],
    },
)
async def _(event):
    "Animation Command"
    try:
        obj = event.pattern_match.group(1)
        if len(obj) != 3:
            return await edit_delete(event, "`Input length must be 3 or empty`")
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    event = await eor(event, "`droping....`")
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            [
                "".join(x)
                for x in (
                    f + (s, g, s + s * f.count(""), t),
                    f + (g, s * 2 + s * f.count(""), t),
                    f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                    f[:i] + (s + s * f.count(""), o, f[i], s, t),
                    f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                    f[:i] + (s * 3 + s * f.count(""), o, t),
                    f[:i] + (s * 3 + s * f.count(""), g, t),
                )
            ]
            for i, f in enumerate(reversed(h))
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            await event.eor(something_else)


@Cyborg.on_cmd(
    pattern="fleaveme$",
    command=("fleaveme", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}fleaveme",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    event = await eor(event, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 10])


@Cyborg.on_cmd(
    pattern="loveu$",
    command=("loveu", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}loveu",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await eor(event, "loveu")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
        "❤",
        "I Love You❤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 35])


@Cyborg.on_cmd(
    pattern="plane$",
    command=("plane", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}plane",
    },
)
async def _(event):
    "animation command"
    event = await eor(event, "Wait for plane...")
    await event.eor("✈-------------")
    await event.eor("-✈------------")
    await event.eor("--✈-----------")
    await event.eor("---✈----------")
    await event.eor("----✈---------")
    await event.eor("-----✈--------")
    await event.eor("------✈-------")
    await event.eor("-------✈------")
    await event.eor("--------✈-----")
    await event.eor("---------✈----")
    await event.eor("----------✈---")
    await event.eor("-----------✈--")
    await event.eor("------------✈-")
    await event.eor("-------------✈")
    await asyncio.sleep(3)


@Cyborg.on_cmd(
    pattern="police$",
    command=("police", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}police",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await eor(event, "Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        f"{mention} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 12])


@Cyborg.on_cmd(
    pattern="jio$",
    command=("jio", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}jio",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(19)
    event = await eor(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Optimising JIO NETWORK...*",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ █`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 19])


@Cyborg.on_cmd(
    pattern="solarsystem$",
    command=("solarsystem", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}solarsystem",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await eor(event, "solarsystem")
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 8])
