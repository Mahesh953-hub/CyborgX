import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url


async def fakegs(search, result):
    imgurl = "https://i.imgur.com/wNFr5X2.jpg"
    with open("./temp/Cyborg.jpg", "wb") as f:
        f.write(requests.get(imgurl).content)
    img = Image.open("./temp/Cyborg.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("userbot/helpers/styles/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("userbot/helpers/styles/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("./temp/Cyborg.jpg")
    return "./temp/Cyborg.jpg"


async def trumptweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.webp", "webp")
    return "Cyborg.webp"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def kannagen(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.webp", "webp")
    return "Cyborg.webp"


async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.webp", "webp")
    return "Cyborg.webp"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.webp", "webp")
    return "Cyborg.webp"


async def iphonex(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png").convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def lolice(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def awooify(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    nadan = r.get("message")
    borgurl = url(nadan)
    if not borgurl:
        return "check syntax once more"
    with open("Cyborg.png", "wb") as f:
        f.write(requests.get(nadan).content)
    img = Image.open("Cyborg.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("Cyborg.jpg", "jpeg")
    return "Cyborg.jpg"
