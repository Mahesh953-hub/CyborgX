from asyncio import sleep
from . import Cyborg

plugin_category = "utils"


@Cyborg.on_cmd(
    pattern=r"schd (\d*) ([\s\S]*)",
    command=("schd", plugin_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    cyborg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cyborg[1]
    ttl = int(cyborg[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
