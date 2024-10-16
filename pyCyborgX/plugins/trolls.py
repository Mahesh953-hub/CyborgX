import os
from telegraph import exceptions, upload_file
from . import Cyborg
from ..funcs.managers import eor
from ..helpers.utils import _cyborgtools, reply_id
from . import convert_toimage, deEmojify, phcomment, threats, trap, trash

plugin_category = "fun"


@Cyborg.on_cmd(
    pattern="trash$",
    command=("trash", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}trash",
    },
)
async def cyborgbot(event):
    "image meme creator."
    replied = await event.get_reply_message()
    cyborgid = await reply_id(event)
    if not replied:
        return await eor(event, "reply to a supported media file")
    output = await _cyborgtools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await event.reply(file=download_location)
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await trash(cyborg)
    os.remove(download_location)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cyborg, reply_to=cyborgid)


@Cyborg.on_cmd(
    pattern="threats$",
    command=("threats", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "usage": "{tr}threats",
    },
)
async def cyborgbot(event):
    "image meme creator."
    replied = await event.get_reply_message()
    cyborgid = await reply_id(event)
    if not replied:
        return await eor(event, "reply to a supported media file")
    output = await _cyborgtools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await threats(cyborg)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cyborg, reply_to=cyborgid)


@Cyborg.on_cmd(
    pattern=r"trap(?:\s|$)([\s\S]*)",
    command=("trap", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "Description": "creates a trap card",
        "usage": "{tr}trap (name of the person to trap) ; (trapper name)",
    },
)
async def cyborgbot(event):
    "image meme creator."
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        text1, text2 = input_str.split(";")
    else:
        return await eor(
            event,
            "**Syntax :** reply to image or sticker with `.trap (name of the person to trap);(trapper name)`",
        )
    replied = await event.get_reply_message()
    cyborgid = await reply_id(event)
    if not replied:
        return await eor(event, "reply to a supported media file")
    output = await _cyborgtools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await trap(text1, text2, cyborg)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cyborg, reply_to=cyborgid)


@Cyborg.on_cmd(
    pattern=r"phub(?:\s|$)([\s\S]*)",
    command=("phub", plugin_category),
    info={
        "header": "Reply to image/sticker to get meme on that image.",
        "description": "pornhub comment creator",
        "usage": "{tr}phub (username);(text in comment)",
    },
)
async def cyborgbot(event):
    "image meme creator."
    input_str = event.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        username, text = input_str.split(";")
    else:
        return await eor(
            event,
            "**Syntax :** reply to image or sticker with `.phub (username);(text in comment)`",
        )
    replied = await event.get_reply_message()
    cyborgid = await reply_id(event)
    if not replied:
        return await eor(event, "reply to a supported media file")
    output = await _cyborgtools.media_to_pic(event, replied)
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    if size > 5242880:
        os.remove(download_location)
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )

    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await output[0].edit(f"**Error: **\n`{exc}`")
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await phcomment(cyborg, text, username)
    await output[0].delete()
    os.remove(download_location)
    await event.client.send_file(event.chat_id, cyborg, reply_to=cyborgid)
