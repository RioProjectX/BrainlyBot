import requests
from pyrogram import Client, filters
from pyrogram.types import Message

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

@Client.on_message(filters.command(["cari"]))
async def brainly(_, message: Message):
    query = get_text(message)
    buttons = [
        [
            InlineKeyboardButton('Anime', url='https://brainly.co.id/app/ask?entry=hero&q='+query),
        InlineKeyboardButton('Cari dengan inline', switch_inline_query_current_chat='cari ')
        ]
    ]
    url = "https://brainly-api.xlaaf.repl.co/br?soal="+query
    hasil = ses.get(url).json()
    subs = hasil['soal']['question']['content']
    nekozu = hasil['jawaban']['content']
    await message.reply_text("**Soal**\n`"+subs+"`\n\n**Jawaban:**\n"+nekozu)
