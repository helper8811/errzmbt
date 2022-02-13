#ChauhanMahesh/Vasusen/DroneBots/COL
from telethon.sessions import StringSession
from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
AU = config("AUTH_USERS", default=None)
CHAT = config("CHAT", default=None, cast=int)

AUTH_USERS = []
y = AU.split(",")
for id in y:
    AUTH_USERS.append(int(id))
    
AUTH = []
x = AU.split(",")
for id in x:
    AUTH.append(id)
    
#connection
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

