#ChauhanMahesh/Vasusen/DroneBots/COL
from telethon.sessions import StringSession
from telethon import TelegramClient
from pyrogram import Client
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 12665045
API_HASH = "d437379dcebbc0a422211503956d8194"
BOT_TOKEN = "6009441071:AAHoB7Jf3CRLTcJlsEcUyVzPKm7I-YwLu7I"
SESSION = "SESSION", default=None
AU = 5288986168
CHAT = int("-1001538922643")
LCHAT = int("-1001538922643")
    
#connection
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

pbot = Client(session_name='pbot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) 

pbot.start()
