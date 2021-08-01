from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram import Client, filters
import requests
import traceback
from pyrogram import errors, __version__
from pyrogram.errors import PeerIdInvalid

ses = requests.session()

@Client.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(query.id,
            results=[
                InlineQueryResultPhoto(
                    caption="Halo! Cari Mau Cari Jawaban Diinline Ya? Pilih Tombol Dibawah",
                    photo_url="https://telegra.ph/file/9dfdfffd59fc5ab836468.jpg",
                    parse_mode="markdown",
                    title=f"Bantuan",
                    description=f"Pencet disini..",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                        InlineKeyboardButton("Channel Bot", url="https://t.me/nekozu"),
                        InlineKeyboardButton(text="Cari", switch_inline_query_current_chat="cari")
                        ]]
                    )
                ),
            ],
            switch_pm_text="Pencet ini Untuk Menuju Pm",
            switch_pm_parameter="start",
            cache_time=300
        )
    answers = []
    if string.split()[0] == "cari":
        if len(string.split()) == 1:
            await client.answer_inline_query(query.id,
                                            results=answers,
                                            switch_pm_text="Cari Pertanyaan Di Private Chat",
                                            switch_pm_parameter="cari"
                                            )
            return
        squery = string.split(None, 1)[1]
        url = "https://brainly-api.xlaaf.repl.co/br?soal="+squery
        hasil = ses.get(url).json()
        brainly = hasil['soal']['question']['content']
        beh = hasil['jawaban']['content']
        pesan = f"**Soal**\n"+brainly+"\n\n**Jawaban:**\n"+beh
        await client.answer_inline_query(query.id,
            results=[
                InlineQueryResultArticle(
                        title="Brainly",
                        description="Cari Brainly",
                        input_message_content=InputTextMessageContent(
                            pesan
                        )
                    )
            ],
            cache_time=1
        )
