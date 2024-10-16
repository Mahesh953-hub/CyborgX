from pyCyborgX import Cyborg
from ..funcs.managers import eor
from ..helpers.utils import _format

plugin_category = "tools"

@Cyborg.on_cmd(
    pattern="json$",
    command=("json", plugin_category),
    info={
        "header": "To get details of that message in json format.",
        "usage": "{tr}json reply to message",
    },
)
async def _(event):
    "To get details of that message in json format."
    cyborgevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = cyborgevent.stringify()
    await eor(event, the_real_message, parse_mode=_format.parse_pre)


@Cyborg.on_cmd(
    pattern="yaml$",
    command=("yaml", plugin_category),
    info={
        "header": "To get details of that message in yaml format.",
        "usage": "{tr}yaml reply to message",
    },
)
async def _(event):
    "To get details of that message in yaml format."
    cyborgevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = _format.yaml_format(cyborgevent)
    await eor(event, the_real_message, parse_mode=_format.parse_pre)
