#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import bot as CA, AUTH_USERS
from .. import CHAT as chat
from telethon import events
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

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
 
#Welcome-------------------------------------------------------------------------

async def get_joiner(id):
    x = True
    try:
        await CA(GetParticipantRequest(channel=int(chat), participant=id))
        x = True
    except UserNotParticipantError:
        x = False
    return x

@CA.on(events.ChatAction(chats=chat))
async def joined(event):
    if event.user_joined or event.user_added:
        user = await event.get_user()
    firstname = user.first_name
    mention = user.username
    if not mention:    
        mention = f"[{firstname}](tg://user?id={user.id})"
    x = await get_joiner(user.id)
    if x is True:
        await CA.send_message(chat , f'`ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴅʀᴏɴᴇ sᴜᴘᴘᴏʀᴛ`\n\n👤 : {mention}\n\n🆔 : `{user.id}`\n\nGreetings by @MaheshChauhan.',
                             buttons=[
                                 [
                                  Button.url("Association", url="t.me/thechariotoflight"),
                                  Button.url("Updates", url="t.me/DroneBots")]])                                              
    else:
        return  
    
    
