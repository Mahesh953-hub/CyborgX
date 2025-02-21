import os
from urllib.request import urlretrieve as donl
from bs4 import BeautifulSoup as bs
from requests import get

from . import *

_base = "https://pinterestdownloader.com/download?url="

plugin_category = "tools"


def gib_link(link):
    colon = "%3A"
    slash = "%2F"
    if link.startswith("https"):
        return _base + link.replace(":", colon).replace("/", slash)
    return _base + f"https{colon}{slash}{slash}pin.it{slash}{link}"


@Cyborg.on_cmd(
    pattern="pntrst ?(.*)",
    command=("pntrst", plugin_category),
    info={
        "header": "Download and send pinterest pins.",
        "description": "you can download and send pinterest video and image.",
        "usage": "{tr}pntrst <link/id>",
    },
)
async def pinterest(e):
    m = e.pattern_match.group(1)
    get_link = get(gib_link(m)).text
    hehe = bs(get_link, "html.parser")
    hulu = hehe.find_all("a", {"class": "download_button"})
    if len(hulu) < 1:
        return await edit_delete(e, "`Wrong link or private pin.`")
    if len(hulu) > 1:
        donl(hulu[0]["href"], "pinterest.mp4")
        donl(hulu[1]["href"], "pinterest.jpg")
        await e.delete()
        await e.client.send_file(
            e.chat_id, "pinterest.mp4", thumb="pinterest.jpg", caption=f"Pin:- {m}"
        )
        os.remove("pinterest.mp4")
        os.remove("pinterest.jpg")
    else:
        await e.delete()
        await e.client.send_file(e.chat_id, hulu[0]["href"], caption=f"Pin:- {m}")
