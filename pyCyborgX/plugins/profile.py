import os
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User
from pyCyborgX import Cyborg
from ..Config import Config
from ..funcs.logger import logging
from ..funcs.managers import edit_delete, eor

LOGS = logging.getLogger(__name__)
plugin_category = "utils"


# ============= CONST =======#
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "```Profile picture changed successfully.```"
PP_TOO_SMOL = "```This image is too small, use a bigger image.```"
PP_ERROR = "```Failure occured while processing image.```"
BIO_SUCCESS = "```Successfully edited Bio.```"
NAME_OK = "```Your name was successfully changed.```"
USERNAME_SUCCESS = "```Your username was successfully changed.```"
USERNAME_TAKEN = "```This username is already taken.```"
#========================#


@Cyborg.on_cmd(
    pattern=r"pbio ([\s\S]*)",
    command=("pbio", plugin_category),
    info={
        "header": "To set bio for this account.",
        "usage": "{tr}pbio <your bio>",
    },
)
async def _(event):
    "To set bio for this account."
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await edit_delete(event, "`successfully changed my profile bio`")
    except Exception as e:
        await eor(event, f"**Error:**\n`{e}`")


@Cyborg.on_cmd(
    pattern=r"pname ([\s\S]*)",
    command=("pname", plugin_category),
    info={
        "header": "To set/change name for this account.",
        "usage": ["{tr}pname firstname ; last name", "{tr}pname firstname"],
    },
)
async def _(event):
    "To set/change name for this account."
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if ";" in names:
        first_name, last_name = names.split(";", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await edit_delete(event, "`My name was changed successfully`")
    except Exception as e:
        await eor(event, f"**Error:**\n`{e}`")


@Cyborg.on_cmd(
    pattern="ppic$",
    command=("ppic", plugin_category),
    info={
        "header": "To set profile pic for this account.",
        "usage": "{tr}ppic <reply to image or gif>",
    },
)
async def _(event):
    "To set profile pic for this account."
    reply_message = await event.get_reply_message()
    cyborgevent = await eor(
        event, "`Downloading Profile Picture to my local ...`"
    )
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e:
        await cyborgevent.eor(str(e))
    else:
        if photo:
            await cyborgevent.eor("`now, Uploading to Telegram ...`")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await cyborgevent.eor("`size must be less than 2 mb`")
                    os.remove(photo)
                    return
                cyborgpic = None
                cyborgvideo = await event.client.upload_file(photo)
            else:
                cyborgpic = await event.client.upload_file(photo)
                cyborgvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(
                        file=cyborgpic, video=cyborgvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:
                await cyborgevent.eor(f"**Error:**\n`{e}`")
            else:
                await eor(
                    cyborgevent, "`My profile picture was successfully changed`"
                )
    try:
        os.remove(photo)
    except Exception as e:
        LOGS.info(str(e))


@Cyborg.on_cmd(
    pattern=r"pusername ([\s\S]*)",
    command=("pusername", plugin_category),
    info={
        "header": "To set/update username for this account.",
        "usage": "{tr}pusername <new username>",
    },
)
async def update_username(event):
    """For .username command, set a new username in Telegram."""
    newusername = event.pattern_match.group(1)
    try:
        await event.client(UpdateUsernameRequest(newusername))
        await edit_delete(event, USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await eor(event, USERNAME_TAKEN)
    except Exception as e:
        await eor(event, f"**Error:**\n`{e}`")


@Cyborg.on_cmd(
    pattern="count$",
    command=("count", plugin_category),
    info={
        "header": "To get your profile stats for this account.",
        "usage": "{tr}count",
    },
)
async def count(event):
    """For .count command, get profile stats."""
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    cyborgevent = await eor(event, "`Processing..`")
    dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            LOGS.info(d)

    result += f"`Users:`\t**{u}**\n"
    result += f"`Groups:`\t**{g}**\n"
    result += f"`Super Groups:`\t**{c}**\n"
    result += f"`Channels:`\t**{bc}**\n"
    result += f"`Bots:`\t**{b}**"

    await cyborgevent.eor(result)


@Cyborg.on_cmd(
    pattern=r"delpfp ?([\s\S]*)",
    command=("delpfp", plugin_category),
    info={
        "header": "To delete profile pic for this account.",
        "description": "If you havent mentioned no of profile pics then only 1 will be deleted.",
        "usage": ["{tr}delpfp <no of pics to be deleted>", "{tr}delpfp"],
    },
)
async def remove_profilepic(delpfp):
    """For .delpfp command, delete your current profile picture in Telegram."""
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await edit_delete(
        delpfp, f"`Successfully deleted {len(input_photos)} profile picture(s).`"
    )


@Cyborg.on_cmd(
    pattern="myusernames$",
    command=("myusernames", plugin_category),
    info={
        "header": "To list public channels or groups created by this account.",
        "usage": "{tr}myusernames",
    },
)
async def _(event):
    "To list all public channels and groups."
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "**Your current reserved usernames are:**\n"
    output_str += "".join(
        f" - {channel_obj.title} @{channel_obj.username} \n"
        for channel_obj in result.chats
    )
    await eor(event, output_str)
