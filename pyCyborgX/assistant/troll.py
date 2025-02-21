import json
import os
import re
from telethon.events import CallbackQuery
from pyCyborgX import Cyborg


@Cyborg.tgbot.on(CallbackQuery(data=re.compile(b"troll_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./pyCyborgX/troll.txt"):
        jsondata = json.load(open("./pyCyborgX/troll.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = userid
            if event.query.user_id in ids:
                reply_pop_up_alert = (
                    "You are not allowed to see this message, better luck next time!"
                )
            else:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
        except KeyError:
            reply_pop_up_alert = "This message no longer exists in CyborgX server"
    else:
        reply_pop_up_alert = "This message no longer exists "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
