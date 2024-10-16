import random
import re
from pyCyborgX import Cyborg
from ..funcs.managers import eor
from . import fonts

plugin_category = "fun"


@Cyborg.on_cmd(
    pattern=r"str(?:\s|$)([\s\S]*)",
    command=("str", plugin_category),
    info={
        "header": "stretches the given text",
        "usage": ["{tr}str <text>", "{tr}str reply this command to text message"],
        "examples": "{tr}str CyborgX",
    },
)
async def stretch(stret):
    "stretches the given text"
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await eor(stret, "`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    count = random.randint(3, 10)
    reply_text = re.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message)
    await eor(stret, reply_text)


@Cyborg.on_cmd(
    pattern=r"zal(?:\s|$)([\s\S]*)",
    command=("zal", plugin_category),
    info={
        "header": "chages given text into some funny way",
        "usage": ["{tr}zal <text>", "{tr}zal reply this command to text message"],
        "examples": "{tr}zal CyborgX",
    },
)
async def zal(zgfy):
    "chages given text into some funny way"
    reply_text = []
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await eor(
            zgfy, "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(3):
            randint = random.randint(0, 2)

            if randint == 0:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[0]).strip()
            elif randint == 1:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + random.choice(fonts.ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await eor(zgfy, "".join(reply_text))


@Cyborg.on_cmd(
    pattern=r"cp(?:\s|$)([\s\S]*)",
    command=("cp", plugin_category),
    info={
        "header": "chages given text into some funny way",
        "usage": ["{tr}cp <text>", "{tr}cp reply this command to text message"],
        "examples": "{tr}cp CyborgX",
    },
)
async def copypasta(cp_e):
    "chages given text into some funny way"
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await eor(cp_e, "`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = random.choice(fonts.EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = random.choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += random.choice(fonts.EMOJIS)
        elif owo in fonts.EMOJIS:
            reply_text += owo
            reply_text += random.choice(fonts.EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            reply_text += owo.upper() if bool(random.getrandbits(1)) else owo.lower()
    reply_text += random.choice(fonts.EMOJIS)
    await eor(cp_e, reply_text)


@Cyborg.on_cmd(
    pattern=r"weeb(?:\s|$)([\s\S]*)",
    command=("weeb", plugin_category),
    info={
        "header": "chages given text into some funny way",
        "usage": ["{tr}weeb <text>", "{tr}weeb reply this command to text message"],
        "examples": "{tr}weeb CyborgX",
    },
)
async def weebify(event):
    "chages given text into some funny way"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "`What I am Supposed to Weebify `")
        return
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in fonts.normiefont:
            weebycharacter = fonts.weebyfont[fonts.normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await eor(event, string)


@Cyborg.on_cmd(
    pattern=r"downside(?:\s|$)([\s\S]*)",
    command=("downside", plugin_category),
    info={
        "header": "chages given text into upside down",
        "usage": [
            "{tr}downside <text>",
            "{tr}downside reply this command to text message",
        ],
        "examples": "{tr}downside CyborgX",
    },
)
async def stylish_generator(event):
    "chages given text into upside down"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for upsidecharacter in string:
        if upsidecharacter in fonts.upsidefont:
            downsidecharacter = fonts.downsidefont[
                fonts.upsidefont.index(upsidecharacter)
            ]
            string = string.replace(upsidecharacter, downsidecharacter)
    await eor(event, string)


@Cyborg.on_cmd(
    pattern=r"subscript(?:\s|$)([\s\S]*)",
    command=("subscript", plugin_category),
    info={
        "header": "chages given text into subscript",
        "usage": [
            "{tr}subscript <text>",
            "{tr}subscript reply this command to text message",
        ],
        "examples": "{tr}subscript CyborgX",
    },
)
async def stylish_generator(event):
    "chages given text into subscript"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            subscriptcharacter = fonts.subscriptfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, subscriptcharacter)
    await eor(event, string)


@Cyborg.on_cmd(
    pattern=r"superscript(?:\s|$)([\s\S]*)",
    command=("superscript", plugin_category),
    info={
        "header": "chages given text into superscript",
        "usage": [
            "{tr}superscript <text>",
            "{tr}superscript reply this command to text message",
        ],
        "examples": "{tr}superscript CyborgX",
    },
)
async def stylish_generator(event):
    "chages given text into superscript"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await eor(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            superscriptcharacter = fonts.superscriptfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, superscriptcharacter)
    await eor(event, string)
