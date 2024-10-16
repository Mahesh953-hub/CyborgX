import os
from pyCyborgX import Cyborg
from ..funcs.managers import edit_delete, eor
from ..helpers import _cyborgutils, reply_id
from . import make_gif

plugin_category = "utils"


@Cyborg.on_cmd(
    pattern=r"collage(?:\s|$)([\s\S]*)",
    command=("collage", plugin_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9>",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    cyborginput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    cyborgid = await reply_id(event)
    event = await eor(
        event, "```collaging this may take several minutes too..... 😁```"
    )
    if not (reply and (reply.media)):
        await event.eor("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cyborgsticker = await reply.download_media(file="./temp/")
    if not cyborgsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(cyborgsticker)
        await event.eor("`Media format is not supported...`")
        return
    if cyborginput:
        if not cyborginput.isdigit():
            os.remove(cyborgsticker)
            await event.eor("`You input is invalid, check help`")
            return
        cyborginput = int(cyborginput)
        if not 0 < cyborginput < 10:
            os.remove(cyborgsticker)
            await event.eor(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        cyborginput = 3
    if cyborgsticker.endswith(".tgs"):
        hmm = await make_gif(event, cyborgsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(cyborgsticker)
            return await event.eor(hmm)
        collagefile = hmm
    else:
        collagefile = cyborgsticker
    endfile = "./temp/collage.png"
    cyborgcmd = f"vcsi -g {cyborginput}x{cyborginput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _cyborgutils.runcmd(cyborgcmd))[:2]
    if not os.path.exists(endfile):
        for files in (cyborgsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await edit_delete(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=cyborgid,
    )
    await event.delete()
    for files in (cyborgsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
