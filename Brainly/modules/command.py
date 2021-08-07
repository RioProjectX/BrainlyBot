import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ses = requests.session()

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.text)
async def brainly(_, message: Message):
    query = get_text(message)
    url = "https://brainly-api.xlaaf.repl.co/br?soal="+query
    hasil = ses.get(url).json()
    subs = hasil['soal']['question']['content']
    nekozu = hasil['jawaban']['content']
    await message.reply("**Soal**\n`"+subs+"`\n\n**Jawaban:**\n"+nekozu)
