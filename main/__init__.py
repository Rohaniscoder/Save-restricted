from os import environ

import logging
import sys
import time

from decouple import config
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

# variables
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
SESSION = environ['SESSION']
FORCESUB = "O_W_B"
AUTH = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client(session_name=SESSION, api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted", bot_token=BOT_TOKEN, api_id=int(API_ID), api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
