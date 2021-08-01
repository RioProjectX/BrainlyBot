# Credits @xditya
import os
import logging
import pyrogram
from decouple import confrom pyrogram import idle, Clientfig


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# vars
APP_ID = config("api_id", default=None, cast=int)
API_HASH = config("api_hash", default=None)
BOT_TOKEN = config("token", default=None)

if __name__ == "__main__" :
    plugins = dict(root="Brainly/modules")
    app = pyrogram.Client(
        "BotzHub",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )

app.start()
idle()
