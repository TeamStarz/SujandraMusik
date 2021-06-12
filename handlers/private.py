from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEKL_1gt842-B5SnR5eHrlBsfTviEt2GwACrAsAAt_YUUnNC_qAE0qWKR8E")
    await message.reply_text(
        f"""Hai 👋🏻, I Am Zeed Music.

I Can Play Music In Your Group's Voice Call. Developed by [Rezy](https://t.me/Reeeeeezy).\n• Add [Me](https://t.me/ZeedRobot) and My [Assistant](https://ZeedAssistance) To Your Group.\n• Give Admin Access To The [Zeed Music](https://t.me/ZeedRobot). 

Happy Listening to the Music!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", url="https://t.me/ZeedGoodBoys/14")
                  ],[
                    InlineKeyboardButton(
                        "Group Music", url="https://t.me/ZeeedMusic"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Rezy_IsBack"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Instagram", url="https://www.instagram.com/ridhoalfahrezi._"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Zeed Music Player Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/Republicfriend")
                ]
            ]
        )
   )


