import sys

from telethon.tl.functions.channels import JoinChannelRequest

import pyCyborgX
from pyCyborgX import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .funcs.logger import logging
from .funcs.session import Cyborg
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("CyborgX")

print(pyCyborgX.__copyright__)
print(f"Licensed under the terms of the {pyCyborgX.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    Cyborg.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class CyborgCheck:
    def __init__(self):
        self.sucess = True


Cyborgcheck = CyborgCheck()
async def hehn():
    try:
        await Cyborg(JoinChannelRequest("@CyborgXUpdates"))
    except BaseException:
        pass


async def startup_process():
    check = await ipchange()
    if check is not None:
        Cyborgcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("Yay your CyborgX Userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if CyborgX is live\
        \nIf you need assistance, head to https://t.me/CyborgXUpdates"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Cyborgcheck.sucess = True
    return


Cyborg.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    Cyborg.disconnect()
elif not Cyborgcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        Cyborg.run_until_disconnected()
    except ConnectionError:
        pass
