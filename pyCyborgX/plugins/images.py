import os
import shutil
from telethon.errors.rpcerrorlist import MediaEmptyError
from pyCyborgX import Cyborg
from ..funcs.managers import eor
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id

plugin_category = "utils"


@Cyborg.on_cmd(
    pattern=r"img(?: |$)(\d*)? ?([\s\S]*)",
    command=("img", plugin_category),
    info={
        "header": "Google image search.",
        "description": "To search images in google. By default will send 3 images.you can get more images(upto 10 only by changing limit value as shown in usage and examples.",
        "usage": ["{tr}img <1-10> <query>", "{tr}img <query>"],
        "examples": [
            "{tr}img 10 CyborgX",
            "{tr}img CyborgX",
            "{tr}img 7 CyborgX",
        ],
    },
)
async def img_sampler(event):
    "Google image search."
    reply_to_id = await reply_id(event)
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await eor(
            event, "Reply to a message or pass a query to search!"
        )
    cyborg = await eor(event, "`Processing...`")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        lim = min(lim, 10)
        if lim <= 0:
            lim = 1
    else:
        lim = 3
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query.replace(",", " "),
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await cyborg.edit(f"Error: \n`{e}`")
    lst = paths[0][query.replace(",", " ")]
    try:
        await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    except MediaEmptyError:
        for i in lst:
            try:
                await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
            except MediaEmptyError:
                pass
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await cyborg.delete()
