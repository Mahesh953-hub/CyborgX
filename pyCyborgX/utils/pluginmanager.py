import importlib
import sys
from pathlib import Path
from pyCyborgX import CMD_HELP, LOAD_PLUG
from ..Config import Config
from ..funcs import LOADED_CMDS, PLG_INFO
from ..funcs.logger import logging
from ..funcs.managers import edit_delete, eor
from ..funcs.session import Cyborg
from ..helpers.tools import media_type
from ..helpers.utils import _format, _cyborgtools, _cyborgutils, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("CyborgX")


def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"pyCyborgX/plugins/{shortname}.py")
        checkplugins(path)
        name = "pyCyborgX.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        if plugin_path is None:
            path = Path(f"pyCyborgX/plugins/{shortname}.py")
            name = f"pyCyborgX.plugins.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Cyborg
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = Cyborg.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._cyborgutils = _cyborgutils
        mod._cyborgtools = _cyborgtools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.eor = eor
        mod.logger = logging.getLogger(shortname)
        mod.borg = Cyborg
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["pyCyborgX.plugins." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    Cyborg.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    try:
        for i in LOAD_PLUG[shortname]:
            Cyborg.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    except BaseException:
        pass
    try:
        name = f"pyCyborgX.plugins.{shortname}"
        for i in reversed(range(len(Cyborg._event_builders))):
            ev, cb = Cyborg._event_builders[i]
            if cb.__module__ == name:
                del Cyborg._event_builders[i]
    except BaseException:
        raise ValueError


def checkplugins(filename):
    with open(filename, "r") as f:
        filedata = f.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as f:
        f.write(filedata)
