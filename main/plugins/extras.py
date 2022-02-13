from telethon import events
import os
from .. import bot as CA
from .. import AU

AUTH_USERS = []
y = AU.split(",")
for id in y:
    AUTH_USERS.append(int(id))
    
AUTH = []
x = AU.split(",")
for id in x:
    AUTH.append(id)

@CA.on(events.NewMessage(incoming=True, pattern=".exzoom"))
async def bash_command(event):
    if not f'{event.sender_id}' in AUTH:
        return
    if not event.is_reply:
        await event.reply("Reply to any txt file!")
        return
    x = await event.get_reply_message()
    try:
        start = (event.text).split(" ")[1]
        end = (event.text).split(" ")[2]  
    except IndexError:
        return await event.reply("Incorrect format.")  
    try:
        if not '.txt' in x.file.name:
            return await event.reply("Reply to a txt file only!")
    except Exception:
        return await event.reply("Reply to a txt file only!")
    reply = await event.reply("Downloading!")          
    file = await event.client.download_media(x.media)
    await reply.edit("Processing!")
    text_file = open(file, "r")
    lines = text_file.read()
    i = 0
    for line in lines.split("\n"):
         try: 
             if 'http' in line:
                 i += 1
                 date_list = line.split("/")
                 date = date_list[4] + '-' + date_list[5] + '-' + date_list[6]     
                 a = line.split(start)[1]
                 link = a.split(end)[0]
                 if not '/' in link:
                     final = 'link no:' + str(i) + '\n\n' + date + '\n\n' + '`https://api.zoom.us/rec/play/' + link + '`'
                     await event.client.send_message(event.chat_id, final) 
         except Exception as e:
             print(e)
             return await event.client.send_message(event.chat_id, f'Link no: {i} Failed!')       
                          
