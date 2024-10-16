import os
from typing import Optional
from moviepy.editor import VideoFileClip
from PIL import Image
from ...funcs.logger import logging
from ...funcs.managers import eor
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    cyborgevent = (
        event
        if noedits
        else await edit_or_reply(event, "`Transfiguration Time! Converting to ....`")
    )
    cyborgmedia = None
    cyborgfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(cyborgfile):
        os.remove(cyborgfile)
    if mediatype == "Photo":
        cyborgmedia = await reply.download_media(file="./temp")
        im = Image.open(cyborgmedia)
        im.save(cyborgfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, cyborgfile, thumb=-1)
    elif mediatype == "Sticker":
        cyborgmedia = await reply.download_media(file="./temp")
        if cyborgmedia.endswith(".tgs"):
            cyborgcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{cyborgmedia}' '{cyborgfile}'"
            stdout, stderr = (await runcmd(cyborgcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif cyborgmedia.endswith(".webp"):
            im = Image.open(cyborgmedia)
            im.save(cyborgfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, cyborgfile, thumb=-1)
        if not os.path.exists(cyborgfile):
            cyborgmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(cyborgfile, 0.1)
            except Exception:
                clip = clip.save_frame(cyborgfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            cyborgmedia = await reply.download_media(file="./temp")
            im = Image.open(cyborgmedia)
            im.save(cyborgfile)
    if cyborgmedia and os.path.lexists(cyborgmedia):
        os.remove(cyborgmedia)
    if os.path.lexists(cyborgfile):
        return cyborgevent, cyborgfile, mediatype
    return cyborgevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
