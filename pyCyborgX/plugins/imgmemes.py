import asyncio
import os
import re
from pyCyborgX import Cyborg
from ..funcs.managers import edit_delete, eor
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@Cyborg.on_cmd(
    pattern=r"fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs CyborgX ; One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    "Fake google search meme"
    text = cyborg.pattern_match.group(1)
    reply_to_id = await reply_id(cyborg)
    if not text:
        if cyborg.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(cyborg, "`What should i search in google.`", 5)
    cate = await eor(cyborg, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            cyborg,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    cyborgfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)


@Cyborg.on_cmd(
    pattern=r"trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump CyborgX is One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    "trump tweet sticker with given custom text_"
    text = cyborg.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cyborg)

    reply = await cyborg.get_reply_message()
    if not text:
        if cyborg.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cyborg, "**Trump : **`What should I tweet`", 5)
    cate = await eor(cyborg, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    cyborgfile = await trumptweet(text)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)


@Cyborg.on_cmd(
    pattern=r"modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi CyborgX is One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    "modi tweet sticker with given custom text"
    text = cyborg.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cyborg)

    reply = await cyborg.get_reply_message()
    if not text:
        if cyborg.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cyborg, "**Modi : **`Btao Kya Likhna Hai ??`", 5)
    cate = await eor(cyborg, "Requesting Modi Ji to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    cyborgfile = await moditweet(text)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)


@Cyborg.on_cmd(
    pattern=r"cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm CyborgX is One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    text = cyborg.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cyborg)

    reply = await cyborg.get_reply_message()
    if not text:
        if cyborg.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cyborg, "`Give text to write on banner, man`", 5)
    cate = await eor(cyborg, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    cyborgfile = await changemymind(text)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)


@Cyborg.on_cmd(
    pattern=r"kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna CyborgX is One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    "kanna chan sticker with given custom text"
    text = cyborg.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cyborg)

    reply = await cyborg.get_reply_message()
    if not text:
        if cyborg.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(cyborg, "**Kanna : **`What should i show you`", 5)
    cate = await eor(cyborg, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    cyborgfile = await kannagen(text)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)


@Cyborg.on_cmd(
    pattern=r"tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; CyborgX is One of the Popular userbot",
    },
)
async def nekobot(cyborg):
    "The desired person tweet sticker with given custom text"
    text = cyborg.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cyborg)

    reply = await cyborg.get_reply_message()
    if not text:
        if cyborg.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                cyborg,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            cyborg,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    cate = await eor(cyborg, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    cyborgfile = await tweets(text, username)
    await cyborg.client.send_file(cyborg.chat_id, cyborgfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)
