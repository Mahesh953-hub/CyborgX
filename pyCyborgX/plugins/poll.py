import random
from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll
from . import Cyborg
from ..funcs.managers import eor
from . import Build_Poll, reply_id

plugin_category = "tools"


@Cyborg.on_cmd(
    pattern=r"poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(cyborgpoll):
    "To create a poll"
    reply_to_id = await reply_id(cyborgpoll)
    string = "".join(cyborgpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await cyborgpoll.client.send_message(
                cyborgpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await cyborgpoll.delete()
        except PollOptionInvalidError:
            await eor(
                cyborgpoll,
                "`A poll option used invalid data (the data may be too long).`",
            )
        except ForbiddenError:
            await eor(cyborgpoll, "`This chat has forbidden the polls`")
        except exception as e:
            await eor(cyborgpoll, str(e))
    else:
        cyborginput = string.split(";")
        if len(cyborginput) > 2 and len(cyborginput) < 12:
            options = Build_Poll(cyborginput[1:])
            try:
                await cyborgpoll.client.send_message(
                    cyborgpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=cyborginput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await cyborgpoll.delete()
            except PollOptionInvalidError:
                await eor(
                    cyborgpoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await eor(cyborgpoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await eor(cyborgpoll, str(e))
        else:
            await eor(
                cyborgpoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
