from .. import bot, pbot

from pyrogram import Client
from telethon import events

@bot.on(events.NewMessage(incoming=True, pattern="!dl1"))
async def dl1(event):
    x = await event.get_reply_message()
    reply = await event.reply("Downloading!")
    msg = await pbot.get_messages(event.sender_id, x.id)
    await reply.edit(await pbot.download_media(msg))
    
@bot.on(events.NewMessage(incoming=True, pattern="!dl2"))
async def dl2(event):
    x = await event.get_reply_message()
    reply = await event.reply("Downloading!")
    await reply.edit(await pbot.download_media(x.media))
