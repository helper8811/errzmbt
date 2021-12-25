#ChauhanMahesh/Vasusen/COL/DroneBots

# (c) Ultroid

import io
import sys
import traceback
import requests
from os import remove

from .. import Drone
from ethon.pyfunc import bash

async def aexec(code, event):
    exec(
        (
            (
                ("async def __aexec(e, client): " + "\n message = event = e")
                + "\n reply = await event.get_reply_message()"
            )
            + "\n chat = (await event.get_chat()).id"
        )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)


def get_paste(data):
    try:
        resp = requests.post("https://hastebin.com/documents", data=data).content
        key = loads(resp)["key"]
        return "haste", key
    except BaseException:
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        return "neko", key

      
async def bash_command(event):
    xx = await eor(event, get_string("com_1"))
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await eor(xx, get_string("devs_1"), time=10)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    stdout, stderr = await bash(cmd)
    OUT = f"**☞ BASH\n\n• COMMAND:**\n`{cmd}` \n\n"
    if stderr:
        OUT += f"**• ERROR:** \n`{stderr}`\n\n"
    if stdout:
        _o = stdout.split("\n")
        o = "\n".join(_o)
        OUT += f"**• OUTPUT:**\n`{o}`"
    if not stderr and not stdout:
        OUT += "**• OUTPUT:**\n`Success`"      
        
        
async def eval(event):
    if len(event.text) > 5 and event.text[5] != " ":
        return await event.reply("insufficient code len.")
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await event.reply("IndrxError!")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "success"
    final_output = (
        "__►__ **EVALPy**\n```{}``` \n\n __►__ **OUTPUT**: \n```{}``` \n".format(
            cmd,
            evaluation,
        )
    )  
