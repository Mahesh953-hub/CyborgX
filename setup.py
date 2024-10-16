import re

import setuptools

requirements = [
    "sqlalchemy==1.4.31",
    "python-decouple",
    "python-dotenv",
    "aiofiles",
    "aiohttp",
    "sqlalchemy-json",
    "pytz",
]


with open("CyborgX/Version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "CyborgX"
author = "RemainsAlways"
description = "A Secure and Powerful Python-Telethon Based Library For CyborgX Userbot."
license_ = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/TeamLionX/LionX"
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license_,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">3.7, <3.11",
)
