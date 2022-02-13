from telethon import events
import os, time
from .. import bot as CA
from .. import AU

from ethon.uploader import ytdl, weburl
from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload
from telethon.tl.types import DocumentAttributeVideo

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
    text_file = open(file)
    lines = text_file.readlines()
    links = []
    for line in lines:
        if 'http' in line:
            links.append(line)
    for i in range(len(links)):
         try: 
             link = links[i]
             date_list = link.split("/")
             date = date_list[4] + '-' + date_list[5] + '-' + date_list[6]     
             a = link.split(start)[1]
             hash = a.split(end)[0]
             final = 'link no:' + str(i + 1) + '\n\n' + date + '\n\n' + '`https://api.zoom.us/rec/play/' + hash + '`'
             await event.client.send_message(event.chat_id, final) 
         except Exception as e:
             print(e)
             return await event.client.send_message(event.chat_id, f'Link no: {i + 1} Failed!')       
                          
@CA.on(events.NewMessage(incoming=True, pattern=".bzoom"))
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
    text_file = open(file)
    lines = text_file.readlines()
    links = []
    for line in lines:
        if 'http' in line:
            links.append(line)
    for i in range(len(links)):
         try: 
             link = links[i]
             date_list = link.split("/")
             date = date_list[4] + '-' + date_list[5] + '-' + date_list[6]     
             a = link.split(start)[1]
             hash = a.split(end)[0]
             await reply.edit(f"Downloading Zoom file\n\nIndex: `{(i + 1)}`\nDate: `{date}`")
             zoom_dl = 'https://api.zoom.us/rec/play/' + hash
             filename = await ytdl(zoom_dl)
             await reply.edit("Preparing to Upload!")
             metadata = video_metadata(filename)
             width = metadata["width"]
             height = metadata["height"]
             duration = metadata["duration"]
             attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
             UT = time.time()
             caption = f'Name: `{filename}`' + f"\n\nIndex: `{(i + 1)}`\nDate: `{date}`" + "\n\n**By @MaheshChauhan**"
             uploader = await fast_upload(f'{filename}', f'{filename}', UT, CA, reply, '**UPLOADING:**')      
             await Drone.send_file(event.chat_id, uploader, caption=caption, thumb=screenshot, attributes=attributes, force_document=False)
             await reply.edit("Sleeping for 5 seconds!")
             time.sleep(5)
         except Exception as e:
             print(e)
             return await event.client.send_message(event.chat_id, f'Link no: {i + 1} Failed!')       
                          
