from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/6c7458e6468f89976bbf0.jpg", caption=f"» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [Rio Projects]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [Support]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 Rio Projects 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
