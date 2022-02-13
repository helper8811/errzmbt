from telethon import events
import os
from .. import bot as CA
from .. import AUTH 

@CA.on(events.NewMessage(incoming=True, from_users=AUTH, pattern=".exzoom"))
async def bash_command(event):
    if not event.is_reply:
        await event.reply('Reply to any txt file!")
        return
    x = await event.get_reply_message()
    try:
        start = (event.text).split(" ")[1]
        end = (event.text).split(" ")[2]  
    except IndexError:
        return await event.reply("Incorrect format.")    
    if not '.txt' in x.file.name:
        return await event.reply("Reply to a txt file only!")
    await event.reply("Downloading!")          
    file = await event.client.download_media(x.media)
    lines = file.readlines()   
                          
