from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>◈ ᴍʏ ɴᴀᴍᴇ :</b> <a href='https://t.me/Pro_ui_bot'>ᴀɴɪ_ᴍɪx*</a> \n<b>◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/B_ani_me'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a> \n<b>◈ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/b_movies_allin1'>ᴍᴏᴠɪᴇ ᴄʀᴜɪsᴇ</a> \n<b>◈ ᴅʀᴀᴍᴀ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/kdrama_in_hindihd'>ᴅʀᴀᴍᴀ ᴄʀᴜɪsᴇ</a> \n<b>◈ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/backup_forall'>ʙᴀᴄᴋ ᴜᴘ</a> \n<b>◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/ad_minn_bot'>ᴀᴅᴍɪɴ</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
