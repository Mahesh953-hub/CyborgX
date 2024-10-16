#!/usr/bin/env python3
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from os import system
print(
    f"""𝐏𝐋𝐄𝐀𝐒𝐄 𝐆𝐎 𝐓𝐎 my.telegram.org
𝐋𝐎𝐆𝐈𝐍 𝐔𝐒𝐈𝐍𝐆 𝐘𝐎𝐔 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐀𝐂𝐂𝐎𝐔𝐍𝐓
𝐂𝐋𝐈𝐂𝐊 𝐎𝐍 𝐀𝐏𝐈 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐌𝐄𝐍𝐓 𝐓𝐎𝐎𝐋𝐒
𝐂𝐑𝐄𝐀𝐓𝐄 𝐀 𝐍𝐄𝐖 𝐀𝐏𝐏𝐋𝐈𝐂𝐀𝐓𝐈𝐎𝐍, 𝐁𝐘 𝐄𝐍𝐄𝐓𝐄𝐑𝐈𝐍𝐆 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃 𝐃𝐄𝐓𝐀𝐈𝐋𝐒""")
NAME = system("figlet CyborgX")
print(f"""𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐂𝐲𝐛𝐨𝐫𝐠𝐗 𝐎𝐧 𝐅𝐢𝐫𝐞  🔥🔥🔥🔥...."""
)
𝐀𝐏𝐏_𝐈𝐃 = int(input("𝐄𝐧𝐭𝐞𝐫 𝐀𝐏𝐏_𝐈𝐃 𝐇𝐞𝐫𝐞: "))
𝐀𝐏𝐈_𝐇𝐀𝐒𝐇 = input("𝐄𝐧𝐭𝐞𝐫 𝐀𝐏𝐈_𝐇𝐀𝐒𝐇 𝐇𝐞𝐫𝐞 : ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
