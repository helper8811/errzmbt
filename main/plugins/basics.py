#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import CA
from telethon import events
from main.plugins.stuff import chat

@CA.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="!rly"))
async def reply(event):
    x = await event.get_reply_message()
    if not x:
        return await event.reply("No message found!")
    try:
        reply_id = int(float((event.text).split(" ")[1]))
    except Exception:
        return await event.reply("No msg id found.")
    await event.client.send_message(chat, x, reply_to=reply_id)
    
@CA.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="!msg"))
async def msg(event):   
    x = await event.get_reply_message()
    if not x:
        return await event.reply("No message found!")
    try:
        msg_id = int(float((event.text).split(" ")[1]))
    except Exception:
        return await event.reply("No msg id found.")
    await event.client.send_message(msg_id, x)
    
    
    
    
    
