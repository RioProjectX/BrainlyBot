from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,                                                                                                                                                                                                 
        text="**Halo Saya Adalah Bot Untuk Mencari Jawaban Dibrainly , Saya Dibuat Oleh @Riio00 !**, Ketik /cari pertanyaan untuk mencari pertanyaan, Bisa menggunakan inline juga loh! Contoh @brainlyriobot cari siapa penemu sepeda?` .",
        reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "👑Developer", url="https://t.me/riio00")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Channel", url="https://t.me/riobotsupport")
                      ]]
                    ))

