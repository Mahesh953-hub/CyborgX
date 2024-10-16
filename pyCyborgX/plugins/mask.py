import os
from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from pyCyborgX import Cyborg
from ..Config import Config
from ..funcs.managers import eor
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_category = "tools"


@Cyborg.on_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(cyborgbot):
    "Hazmat suit maker"
    reply_message = await cyborgbot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await eor(cyborgbot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await eor(cyborgbot, "```Reply to actual users message.```")
    event = await cyborgbot.eor("```Processing```")
    async with cyborgbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await cyborgbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.eor(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.eor(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await cyborgbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@Cyborg.on_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def cyborgbot(cyborgmemes):
    "replied Image will be face of other image"
    replied = await cyborgmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(cyborgmemes, "reply to a supported media file")
    if replied.media:
        cyborgevent = await eor(cyborgmemes, "passing to telegraph...")
    else:
        return await eor(cyborgmemes, "reply to a supported media file")
    download_location = await cyborgmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await cyborgevent.eor(
                "the replied file size is not supported it must me below 5 mb"
            )
        await cyborgevent.eor("generating image..")
    else:
        os.remove(download_location)
        return await cyborgevent.eor("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await cyborgevent.eor("ERROR: " + str(exc))
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await awooify(cyborg)
    await cyborgevent.delete()
    await cyborgmemes.client.send_file(cyborgmemes.chat_id, cyborg, reply_to=replied)


@Cyborg.on_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def cyborgbot(cyborgmemes):
    "replied Image will be face of other image"
    replied = await cyborgmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(cyborgmemes, "reply to a supported media file")
    if replied.media:
        cyborgevent = await eor(cyborgmemes, "passing to telegraph...")
    else:
        return await eor(cyborgmemes, "reply to a supported media file")
    download_location = await cyborgmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await cyborgevent.eor(
                "the replied file size is not supported it must me below 5 mb"
            )
        await cyborgevent.eor("generating image..")
    else:
        os.remove(download_location)
        return await cyborgevent.eor("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await cyborgevent.eor("ERROR: " + str(exc))
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await lolice(cyborg)
    await cyborgevent.delete()
    await cyborgmemes.client.send_file(cyborgmemes.chat_id, cyborg, reply_to=replied)


@Cyborg.on_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def cyborgbot(cyborgmemes):
    "replied Image will be face of other image"
    replied = await cyborgmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(cyborgmemes, "reply to a supported media file")
    if replied.media:
        cyborgevent = await eor(cyborgmemes, "passing to telegraph...")
    else:
        return await eor(cyborgmemes, "reply to a supported media file")
    download_location = await cyborgmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await cyborgevent.eor(
                "the replied file size is not supported it must me below 5 mb"
            )
        await cyborgevent.eor("generating image..")
    else:
        os.remove(download_location)
        return await cyborgevent.eor("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await cyborgevent.eor("ERROR: " + str(exc))
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await baguette(cyborg)
    await cyborgevent.delete()
    await cyborgmemes.client.send_file(cyborgmemes.chat_id, cyborg, reply_to=replied)


@Cyborg.on_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def cyborgbot(cyborgmemes):
    "replied image as iphone x wallpaper."
    replied = await cyborgmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(cyborgmemes, "reply to a supported media file")
    if replied.media:
        cyborgevent = await eor(cyborgmemes, "passing to telegraph...")
    else:
        return await eor(cyborgmemes, "reply to a supported media file")
    download_location = await cyborgmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await cyborgevent.eor(
                "the replied file size is not supported it must me below 5 mb"
            )
        await cyborgevent.eor("generating image..")
    else:
        os.remove(download_location)
        return await cyborgevent.eor("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await cyborgevent.eor("ERROR: " + str(exc))
    cyborg = f"https://telegra.ph{response[0]}"
    cyborg = await iphonex(cyborg)
    await cyborgevent.delete()
    await cyborgmemes.client.send_file(cyborgmemes.chat_id, cyborg, reply_to=replied)
