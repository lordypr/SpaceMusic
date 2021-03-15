from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo Kawan {message.from_user.first_name}!</b>
Gua adalah Bot Music Voice Call Group di Telegram!

Gua Hadir Untuk Menemani Kegabutan Lu! Lu Bisa Menggunakan Gua Dengan Cara Yang Ada Dibawah. Jangan Malas Untuk Membaca Ya Pantek!
JANGAN LUPA LIHAT BIO DAN DESKRIPSI BOTNYA!

Cara Menggunakan Bot Ini Mudah, Cukup Undang Bot Ini Dan Assistantnya Kegrup Lu Aja Lalu Berikan Akses Admin.

TEKAN TOMBOL DIBAWAH UNTUK TUTORIAL! JANGAN MALAS MEMBACA....""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(https://telegra.ph/Tutorial-03-15-2"
                        "CARA MENGGUNAKANNYA", "
                   ),
                    InlineKeyboardButton(
                        "GROUP 💬 ", url="https://t.me/urmoodzone"
                   )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Halo, Mau Mencari Lagu?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
