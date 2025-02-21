import os
import random
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos
from . import Cyborg, mention

plugin_category = "tools"

PICS_STR = []


@Cyborg.on_cmd(
    pattern="rlogo ?(.*)",
    command=("rlogo", plugin_category),
    info={
        "header": "Logo Maker Plugin",
        "examples": "{tr}llogo Enjoyer",
        "usage": [
            "{tr}rlogo <your name>",
            "{tr}rlogo <your name> <reply to a pic>",
        ],
    },
)
async def Logo(odi):
    evxnt = await odi.edit("`processing ...`")
    text = odi.pattern_match.group(1)
    if not text:
        await evxnt.edit("`Give some text to make a logo`")
        return
    fnt = await get_font_file(odi.client, "@FontsBin")
    if odi.reply_to_msg_id:
        rply = await odi.get_reply_message()
        logo_ = await rply.download_media()
    else:
        async for i in bot.iter_messages(f"@BgBin", filter=InputMessagesFilterPhotos):
            PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
    if len(text) <= 8:
        font_size_ = 150
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 130
        strik = 20

    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fnt, font_size_)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        text,
        font=font,
        fill=(255, 255, 255),
    )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text(
        (w_, h_), text, font=font, fill="white", stroke_width=strik, stroke_fill="black"
    )
    file_name = "Logo.png"
    img.save(
        file_name,
        "png",
    )
    await bot.send_file(odi.chat_id, file_name, caption=f"**Generated By:** {mention}")
    await evxnt.delete()
    try:
        os.remove(file_name)
        os.remove(fnt)
        os.remove(logo_)
    except:
        pass


async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id, filter=InputMessagesFilterDocument, limit=None
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)
