from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import Cyborg
from ..funcs.managers import eor

plugin_category = "tools"


@Cyborg.on_cmd(
    pattern=r"firmware ([\s\S]*)",
    command=("firmware", plugin_category),
    info={
        "header": "To get lastest Firmware.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}firmware <codename>",
        "examples": "{tr}firmware whyred",
    },
)
async def _(event):
    "To get lastest Firmware."
    link = event.pattern_match.group(1)
    firmware = "firmware"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"vendor ([\s\S]*)",
    command=("vendor", plugin_category),
    info={
        "header": "To get lastest Vendor.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}vendor <codename>",
        "examples": "{tr}vendor whyred",
    },
)
async def _(event):
    "To get lastest Vendor."
    link = event.pattern_match.group(1)
    vendor = "vendor"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"xspecs ([\s\S]*)",
    command=("xspecs", plugin_category),
    info={
        "header": "To get quick spec information about device",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}xspecs <codename>",
        "examples": "{tr}xspecs whyred",
    },
)
async def _(event):
    "To get quick spec information about device"
    link = event.pattern_match.group(1)
    specs = "specs"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"fastboot ([\s\S]*)",
    command=("fastboot", plugin_category),
    info={
        "header": "To get latest fastboot MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}fastboot <codename>",
        "examples": "{tr}fastboot whyred",
    },
)
async def _(event):
    "To get latest fastboot MIUI."
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"recovery ([\s\S]*)",
    command=("recovery", plugin_category),
    info={
        "header": "To get latest recovery MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}recovery <codename>",
        "examples": "{tr}recovery whyred",
    },
)
async def _(event):
    "To get latest recovery MIUI."
    link = event.pattern_match.group(1)
    recovery = "recovery"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"pb ([\s\S]*)",
    command=("pb", plugin_category),
    info={
        "header": "To get latest PBRP.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}pb <codename>",
        "examples": "{tr}pb whyred",
    },
)
async def _(event):
    "To get latest PBRP."
    link = event.pattern_match.group(1)
    pitch = "pb"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@Cyborg.on_cmd(
    pattern=r"of ([\s\S]*)",
    command=("of", plugin_category),
    info={
        "header": "To get latest ORangeFox Recover.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}of <codename>",
        "examples": "{tr}of whyred",
    },
)
async def _(event):
    "To get latest ORangeFox Recover."
    link = event.pattern_match.group(1)
    ofox = "of"
    cyborgevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await cyborgevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await cyborgevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)
