import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bf88f56c511e27016cb9a.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝐾𝐴𝐴𝐿🔥](https://t.me/its_heaven_King)

𝑪𝒓𝒆𝒂𝒕𝒐𝒓 :- [✨ 𝐾𝐴𝐴𝐿](https://t.me/its_heaven_king)
𝑺𝒖𝒑𝒑𝒐𝒓𝒕 :- [✨ 𝑲𝑨𝑨𝑳 𝑩𝑶𝑻𝑺❤️](https://t.me/KAAL_BOTS_SUPPORT)
𝑫𝒊𝒔𝒄𝒖𝒔𝒔 :- [✨  𝑨𝒊𝒎 𝒕𝒐 𝑵𝑬𝑬𝑻](https://t.me/AIMTONEET)
『Kᴀᴀʟ』𝑭𝑬𝑬𝑳𝑰𝑵𝑮𝑺ツ :- [✨ 𝗝𝗼𝗶𝗻 ](https://t.me/bad_boy_kaal)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝑲𝒂𝒂𝒍😎](https://t.me/its_heaven_king)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝑱𝑶𝑰𝑵 𝑨𝑵𝑫 𝑺𝑼𝑷𝑷𝑶𝑹𝑻 ✨", url=f"https://t.me/KAAL_BOTS_SUPPORT")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bf88f56c511e27016cb9a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝑺𝑶𝑼𝑹𝑪𝑬 𝑪𝑶𝑫𝑬 💞", url=f"https://github.com/garwmishra/KAAL-MUSIC")
                ]
            ]
        ),
    )
