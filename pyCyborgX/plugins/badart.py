"""
@CyborgXUpdates
"""

import asyncio

from ..funcs.managers import eor
from . import Cyborg, mention

plugin_category = "fun"


# ==================================================================

C = (
    "\n......................................../´¯/) "
    "\n......................................,/¯../ "
    "\n...................................../..../ "
    "\n..................................../´.¯/"
    "\n..................................../´¯/"
    "\n..................................,/¯../ "
    "\n................................../..../ "
    "\n................................./´¯./"
    "\n................................/´¯./"
    "\n..............................,/¯../ "
    "\n............................./..../ "
    "\n............................/´¯/"
    "\n........................../´¯./"
    "\n........................,/¯../ "
    "\n......................./..../ "
    "\n....................../´¯/"
    "\n....................,/¯../ "
    "\n.................../..../ "
    "\n............./´¯/'...'/´¯¯`·¸ "
    r"\n........../'/.../..../......./¨¯\ "
    "\n........('(...´...´.... ¯~/'...') "
    r"\n.........\.................'...../ "
    r"\n..........''...\.......... _.·´ "
    r"\n............\..............( "
    r"\n..............\.............\..."
)


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# =======================================================


@Cyborg.on_cmd(
    pattern="muth$",
    command=("muth", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}muth",
    },
)
async def kakashi(bsdk):
    "Bad stuff"
    animation_interval = 0.3
    animation_ttl = range(100)
    bsdk = await eor(bsdk, "**Ahhhhhhhh......**💦💦...")
    animation_chars = [
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8===✊️D💦",
        "8==✊️=D💦💦",
        "8=✊️==D💦💦💦",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await bsdk.eor(animation_chars[i % 10])


@Cyborg.on_cmd(
    pattern="ohnoo$",
    command=("ohnoo", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}ohnoo",
    },
)
async def kakashi(bsdk):
    "Bad stuff"
    animation_interval = 1
    animation_ttl = range(11)
    bsdk = await eor(bsdk, "**Ohhh nooooo **💦💦...")
    animation_chars = [
        "**Ohhh Baby..**😈",
        r"__**Ohh Yeaah..**__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        r"__**Ohh ohhh..**__\n\n 😈\n  |\  \n  |  \   \n  8=👊-D\n  |   \         \n 👟 👟       😲",
        r"__**Ohh.. **__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        r"__**Ohh baby..**__\n\n 😈\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         \n 👟 👟       😲",
        r"__**Yeaah..**__\n\n 😣\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       😲",
        r"__**Yeaah Yaaah..**__\n\n 😣\n  |\  \n  |  \   \n  8=👊-D💦\n  |   \         💦\n 👟 👟       😲",
        r"__**Yaah baby..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        r"__**Ohhh..**__\n\n 😍\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        r"__**Love u..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       🤤",
        r"__**Love u babe**__\n\n 😍\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       🤤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await bsdk.eor(animation_chars[i % 11])


@Cyborg.on_cmd(
    pattern="lovestory$",
    command=("lovestory", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}lovestory",
    },
)
async def kakashi(event):
    "Bad stuff"
    animation_interval = 3
    animation_ttl = range(14)
    event = await eor(event, "Starting asf")
    animation_chars = [
        "1 ❤️ love story",
        r"  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        r"  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        r"  😚            😒 \n/👕\         <👗> \n  👖             /|",
        r"  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        r"  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        r"  😘   😊 \n /👕\/👗\ \n   👖   /|",
        r" 😳  😁 \n /|\ /👙\ \n /     / |",
        r"😈    /😰\ \n<|\      👙 \n /🍆    / |",
        r"😅 \n/(),✊😮 \n /\         _/\\/|",
        "😎 \n/\\_,__😫 \n  //    //       \\",
        "😖 \n/\\_,💦_😋  \n  //         //        \\",
        r"  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "The End 😂...",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.eor(animation_chars[i % 14])


@Cyborg.on_cmd(
    pattern="ohhyaah$",
    command=("ohhyaah", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}ohhyaah",
    },
)
async def kakashi(baby):
    "Bad stuff"
    await eor(
        baby,
        "**💪💪Ohhh Yeeah Baby**...\n\n"
        "／ イ  ..........(((ヽ   \n"
        "(  ﾉ       ￣—--＼    \n"
        r"| (＼  (\🎩/)   ｜    )  \n"
        "ヽ ヽ` ( ͡° ͜ʖ ͡°) _ノ    /  \n"
        " ＼ | ⌒Ｙ⌒ /  /  \n"
        "   ｜ヽ  ｜  ﾉ ／  \n"
        "     ＼トー仝ーイ \n"
        "        ｜ ミ土彡/ \n"
        r"         ) \      °   /  \n"
        r"        (     \🌿 /  \n"
        "         /       /ѼΞΞΞΞΞΞΞD💨💦\n"
        r"      /  /     /      \ \   \  \n"
        "      ( (    ).           ) ).  ) \n"
        "     (      ).            ( |    | \n"
        r"      |    /                \    |\n"
        "      👞.                  👞",
    )


@Cyborg.on_cmd(
    pattern="foff$",
    command=("foff", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}foff",
    },
)
async def kakashi(fooku):
    "Bad stuff"
    await eor(
        fooku,
        ".                       /¯ )\n"
        "                      /¯  /\n"
        "                    /    /\n"
        "              /´¯/'   '/´¯¯`•¸\n"
        r"          /'/   /    /       /¨¯\ \n"
        "        ('(   (   (   (  ¯~/'  ')\n"
        r"         \                        /\n"
        r"          \                _.•´\n"
        r"            \              (\n"
        r"              \  \n"
        "Roses are RED\n"
        "Violets are BLUE\n"
        "This is my middle finger\n"
        "It just for U🖕😂\n",
    )


@Cyborg.on_cmd(
    pattern="mf$",
    command=("mf", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}mf",
    },
)
async def kakashi(mf):
    "Bad stuff"
    await eor(mf, C)


@Cyborg.on_cmd(
    pattern="sporn$",
    command=("sporn", plugin_category),
    info={
        "header": "bad animation, try yourself ",
        "usage": "{tr}sporn",
    },
)
async def kakashi(pornhub):
    "Bad stuff"
    await eor(
        pornhub,
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⠀⢠⣤⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠸⠿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⠿⠷⣤⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡏⢀⣤⣤⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡇⠘⠿⠿⠃⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠦⠤⠤⠴⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⣄⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠉⠉⢉⣉⣉⣉⣉⣉⣉⡉⠉⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠻⠿⠿⠿⣿⡿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣤⣤⣤⣤⣾⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⢉⣩⣭⣭⣭⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣿⡟⠋⠉⠋⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣾⣿⣶⣶⣶⡆⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣶⣶⣶⣶⣶⣶⣶⡆⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣾⣏⠀⠀⣹⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠘⠿⠿⠿⠟⠃⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n",
    )


@Cyborg.on_cmd(
    pattern="spika$",
    command=("spika", plugin_category),
    info={
        "header": "bad art, try yourself ",
        "usage": "{tr}spika",
    },
)
async def kakashi(pikachu):
    "Bad stuff"
    await eor(
        pikachu,
        "⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿\n"
        "⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
        "⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠻⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
        "⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠸⣿⣿⣿\n"
        "⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠀⠤⠄⠀⠀⠉⠁⠀⠀⠀⢿⣿⣿\n"
        "⣿⣿⣿⣿⠀⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠠⣿⣿⣷⠀⣿⣿\n"
        "⣿⣿⣿⣿⡀⠀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠉⠉⠁⠀⣿⣿\n"
        "⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿🅼🅰️ 🅺🅸 🅲🅷🆄⢸⣿⣿⣿⣿⣿⣿\n"
        "🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️🅲🅷🆄\n",
    )


@Cyborg.on_cmd(
    pattern="sxx$",
    command=("sxx", plugin_category),
    info={
        "header": "bad art, try yourself ",
        "usage": "{tr}sxx",
    },
)
async def kakashi(saxy):
    "Bad stuff"
    await eor(
        saxy,
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀\n"
        "⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀\n"
        "⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀\n"
        "⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀\n"
        "⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦\n"
        "⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟\n"
        "⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
        "⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀\n"
        "⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀\n"
        "⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀\n"
        "⠄⠄⠄⠄⠄⠄⣠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠄⠄⠄\n"
        "⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄\n"
        "⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄\n"
        "⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄\n"
        "⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄\n"
        "⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄\n"
        "⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆\n"
        "⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇\n"
        "⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇\n"
        "⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄\n"
        "⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇⠄\n"
        "⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄\n"
        "⠄⠄⠄⢹⠣⣛⣣⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄\n"
        "⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀\n"
        "⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⡆\n"
        "⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿\n"
        "⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿\n"
        "⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡟\n"
        "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⡟\n"
        "⣸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⡿⢟⣣\n"
        "ɮǟȶǟʊ ȶɦǟʀӄɨօ ӄʏǟ ɦǟǟʟ ,ӄɛֆǟ ʟǟɢǟ\n",
    )


@Cyborg.on_cmd(
    pattern=r"sdick ([\s\S]*)",
    command=("sdick", plugin_category),
    info={
        "header": "bad art, try yourself ",
        "usage": "{tr}sdick <text>",
    },
)
async def kakashi(dicksay):
    "Bad stuff"
    text = dicksay.pattern_match.group(1)
    await eor(
        dicksay,
        f"**{mention} ➥ {text} .\n**"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n",
    )


@Cyborg.on_cmd(
    pattern=r"^\.(?:penis|dick)\s?(.)?",
    command=("penis|dick", plugin_category),
    info={
        "header": "bad art, try yourself ",
        "usage": "{tr}penis",
    },
)
async def kakashi(e):
    "Bad stuff"
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.eor(titid)
