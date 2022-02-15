import os, time, subprocess, asyncio
from pathlib import Path

from .. import bot as CA
from .. import AU

from ethon.uploader import ytdl, weburl
from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload

from telethon import events
from telethon.tl.types import DocumentAttributeVideo
    
AUTH = []
x = AU.split(",")
for id in x:
    AUTH.append(id)
    
async def screenshot(video, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    out = f"{(str(video)).split(".")[0]}.jpg"
    cmd = f'ffmpeg -ss 00:15:00 -i """{video}""" -vframes 1 """{out}""" -y'.split(" ")
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
        
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    print(x)
    print(y)
    if os.path.isfile(out):
        return out
    else:
        None
        
@CA.on(events.NewMessage(incoming=True, pattern=".exzoom"))
async def exzoom(event):
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
async def bzoom(event):
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
    date = ""
    zoom_dl = ""
    for line in lines:
        if 'http' in line:
            links.append(line)
    for i in range(len(links)):
         try: 
             try:
                 link = links[i]
                 date_list = link.split("/")
                 date = date_list[4] + '-' + date_list[5] + '-' + date_list[6]     
                 a = link.split(start)[1]
                 hash = a.split(end)[0]
                 zoom_dl = 'https://api.zoom.us/rec/play/' + hash
             except Exception:
                 date = 'unkown'
                 zoom_dl = links[i]
             await reply.edit(f"Downloading Zoom file\n\nIndex: `{(i + 1)}`\nDate: `{date}`")
             filename = await ytdl(zoom_dl)
             await reply.edit("Preparing to Upload!")
             metadata = video_metadata(filename)
             width = metadata["width"]
             height = metadata["height"]
             duration = metadata["duration"]
             attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
             thumb = await screenshot(filename, event.sender_id)
             UT = time.time()
             caption = f'Name: `{filename}`' + f"\n\nIndex: `{(i + 1)}`\nDate: `{date}`" + "\n\n**By @MaheshChauhan**"
             uploader = await fast_upload(f'{filename}', f'{filename}', UT, CA, reply, '**UPLOADING:**')      
             await CA.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, attributes=attributes, force_document=False)
             await reply.edit("Sleeping for 5 seconds!")
             time.sleep(5)
         except Exception as e:
             print(e)
             return await event.client.send_message(event.chat_id, f'Link no: {i + 1} Failed!')             
    await reply.delete()
    await event.client.send_message(event.chat_id, f'`{len(links)}` uploaded Successfully!')
