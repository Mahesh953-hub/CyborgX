from telethon.errors.rpcerrorlist import YouBlockedUserError
from ..funcs.managers import edit_delete, eor
from . import Cyborg, reply_id

plugin_category = "fun"


async def mememaker(borg, msg, cyborg, chat_id, reply_to_id):
    async with borg.conversation("@themememakerbot") as conv:
        try:
            msg = await conv.send_message(msg)
            pic = await conv.get_response()
            await borg.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await cyborg.edit("Please unblock @themememakerbot and try again")
            return
        await cyborg.delete()
        await borg.send_file(
            chat_id,
            pic,
            reply_to=reply_to_id,
        )
    await borg.delete_messages(conv.chat_id, [msg.id, pic.id])


@Cyborg.on_cmd(
    pattern=r"fox ?([\s\S]*)",
    command=("fox", plugin_category),
    info={
        "header": "fox meme",
        "description": "Send sneeky fox troll",
        "usage": "{tr}fox <text>",
    },
)
async def cyborg(event):
    "sneeky fox troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await edit_delete(event, "`Give me some text to process...`")
    msg = f"/sf {input_text}"
    cyborg = await eor(event, "```Fox is on your way...```")
    await mememaker(event.client, msg, cyborg, event.chat_id, reply_to_id)


@Cyborg.on_cmd(
    pattern=r"talkme ?([\s\S]*)",
    command=("talkme", plugin_category),
    info={
        "header": "talk to me meme",
        "description": "Send talk to me troll",
        "usage": "{tr}talkme <text>",
    },
)
async def cyborg(event):
    "talk to me troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await edit_delete(event, "`Give me some text to process...`")
    msg = f"/ttm {input_text}"
    cyborg = await eor(event, "```Wait making your hardcore meme...```")
    await mememaker(event.client, msg, cyborg, event.chat_id, reply_to_id)


@Cyborg.on_cmd(
    pattern=r"slip ?([\s\S]*)",
    command=("slip", plugin_category),
    info={
        "header": "brain say meme",
        "description": "Send you a sleeping brain meme.",
        "usage": "{tr}slip <text>",
    },
)
async def cyborg(event):
    "Sleeping brain meme."
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await edit_delete(event, "`Give me some text to process...`")
    msg = f"/bbn {input_text}"
    cyborg = await eor(event, "```You can't sleep...```")
    await mememaker(event.client, msg, cyborg, event.chat_id, reply_to_id)


@Cyborg.on_cmd(
    pattern=r"sbob ?([\s\S]*)",
    command=("sbob", plugin_category),
    info={
        "header": "spongebob meme",
        "description": "Send you spongebob meme.",
        "usage": "{tr}sbob <text>",
    },
)
async def cyborg(event):
    "spongebob troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await edit_delete(event, "`Give me some text to process...`")
    msg = f"/sp {input_text}"
    cyborg = await eor(event, "```Yaah wait for spongebob...```")
    await mememaker(event.client, msg, cyborg, event.chat_id, reply_to_id)


@Cyborg.on_cmd(
    pattern=r"child ?([\s\S]*)",
    command=("child", plugin_category),
    info={
        "header": "child meme",
        "description": "Send you child in trash meme.",
        "usage": "{tr}child <text>",
    },
)
async def cyborg(event):
    "child troll"
    reply_to_id = await reply_id(event)
    input_text = event.pattern_match.group(1)
    if not input_text:
        return await edit_delete(event, "`Give me some text to process...`")
    msg = f"/love {input_text}"
    cyborg = await eor(event, "```Wait for your son......```")
    await mememaker(event.client, msg, cyborg, event.chat_id, reply_to_id)
