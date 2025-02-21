from geopy.geocoders import Nominatim
from telethon.tl import types
from pyCyborgX import Cyborg
from ..funcs.managers import eor
from ..helpers import reply_id

plugin_category = "tools"


@Cyborg.on_cmd(
    pattern=r"gps ([\s\S]*)",
    command=("gps", plugin_category),
    info={
        "header": "To send the map of the given location.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "Map of the given location."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    cyborgevent = await eor(event, "`finding.....`")
    geolocator = Nominatim(user_agent="CyborgX")
    if geoloc := geolocator.geocode(input_str):
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**Location : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await cyborgevent.delete()
    else:
        await cyborgevent.edit("`i coudn't find it`")
