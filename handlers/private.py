import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96141420c023cd3227f6b.jpg",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ = [๐พ๐ด๐ด๐ฟ๐ฅ](https://t.me/its_heaven_King)

๐ช๐๐๐๐๐๐ :- [๐ฅ๐๐๐๐๐๐ ๐๐๐๐๐ฅ](https://t.me/its_heaven_king)
๐ถ๐๐๐๐  :- [๐๐๐ ๐๐ข๐ซ๐ฅ](https://t.me/its_vip_girl)
๐บ๐๐๐๐๐๐ :- [โจ ๐ฒ๐จ๐จ๐ณ ๐ฉ๐ถ๐ป๐บโค๏ธ](https://t.me/KAAL_BOTS_SUPPORT)
๐ซ๐๐๐๐๐๐ :- [โจ  ๐๐๐ ๐๐ฎ๐ง๐ข๐ฒ๐](https://t.me/vip_dunia)
ใKแดแดสใ๐ญ๐ฌ๐ฌ๐ณ๐ฐ๐ต๐ฎ๐บใ :- [โจ ๐๐ผ๐ถ๐ป ](https://t.me/bad_boy_kaal)

๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐จ๐ฌ๐ฌ = [๐ฒ๐๐๐๐](https://t.me/its_heaven_king)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ ๐ฑ๐ถ๐ฐ๐ต ๐จ๐ต๐ซ ๐บ๐ผ๐ท๐ท๐ถ๐น๐ป โจ", url=f"https://t.me/KAAL_BOTS_SUPPORT")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96141420c023cd3227f6b.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ ๐บ๐ถ๐ผ๐น๐ช๐ฌ ๐ช๐ถ๐ซ๐ฌ ๐", url=f"https://github.com/garwmishra/KAAL-MUSIC")
                ]
            ]
        ),
    )
