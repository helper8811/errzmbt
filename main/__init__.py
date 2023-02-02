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
SESSION = config("AQDCiriaFyuy_nKp5UbrtyDCIiZ9R6jWnT0GNxo3e4xL_LZ6RQrlzSiupopLvHzd4SgjW1zZx5JRFeQqHhfTUz2-zlYRkx53rj7Us0pGdIKiQCQDw6V0m9kOVtYR4QsUjt5PcUmL9JFHJH2GXSf3NAXV0-XNaliY_vphUnYI7zQkBjgd7a5ktXQxnfq-kBswHDEldaqhs-xA52kVpR37h41VRFiPV2WLwRqOb7hhTuNT6pk5A85g1d3hEqQKx1KEb3hx7GMxLYqsIhuLXdzphlu7ozAElR36bOCwnivhLYlDOLYqWtUh1NxMAST4voPwgbF-4Bv88dRjyu56eMAyzIm6AAAAATs_hjgA", default=None)
AU = config("5288986168", default=None)
CHAT = config("1538922643", default=None, cast=int)
LCHAT = config("1538922643", default=None)
    
#connection
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

pbot = Client(session_name='pbot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) 

pbot.start()
