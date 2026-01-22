from bot import bot
import time
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class RateLimiter:
    def __init__(self, limit=25, interval=1.0):
        self.score = 0
        self.limit = limit
        self.interval = interval

    async def acquire(self):
        while self.score >= self.limit:
            await asyncio.sleep(self.interval)
            self.score = 0
        self.score += 1
limiter = RateLimiter()


async def safe_send(send_func, *args, **kwargs):
    try:
        await limiter.acquire()
        result = await send_func(*args, **kwargs)
        print(f"[SAFE_SEND] {send_func.__name__}: {limiter.score}")
        return result
    except Exception as e:
        print(f"[ERROR] safe_send: {e}\n{args}\n{send_func}")
        return None


async def answer(id_, text):
    msg = await safe_send(bot.send_message,id_,text,protect_content=True)
    return msg.message_id
async def reply(message, text):
    await safe_send(message.reply, text)
    return msg.message_id

async def dropvoice(user_id, file_id):
    msg = await safe_send(bot.send_voice, user_id, file_id)
    return msg.message_id
async def drop_video_note(user_id, file_id):
    msg = await safe_send(bot.send_video_note, user_id, file_id)
    return msg.message_id
async def dropaudio(user_id, file_id):
    msg = await safe_send(bot.send_audio, user_id, file_id)
    return msg.message_id
async def dropsticker(user_id, file_id):
    msg = await safe_send(bot.send_sticker, user_id, file_id)
    return msg.message_id
async def dropgif(user_id, file_id):
    msg = await safe_send(bot.send_animation, user_id, file_id)
    return msg.message_id
async def dropmedia(user_id, media):
    msg = await safe_send(bot.send_media_group, user_id, media)
    return msg.message_id
async def dropphoto_html(user_id, photo_id, text =''):
    msg = await safe_send(bot.send_photo, user_id, photo_id, caption=text, parse_mode='HTML')
    return msg.message_id
async def dropphoto(user_id, photo_id, text=''):
    msg = await safe_send(bot.send_photo, user_id, photo_id, caption=text)
    return msg.message_id
async def delete_message(chat_id, mess_id):
    try:
        await safe_send(bot.delete_message, chat_id, mess_id)
    except Exception:
        pass

async def dropkeyboard(user_id: int, one_time, buttons: list[str], text: str = ""):
    keyboard = [
        [KeyboardButton(text=b) for b in buttons[i:i + 4]]
        for i in range(0, len(buttons), 4)
    ]

    kb = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard = one_time
    )

    msg = await safe_send(bot.send_message,
        chat_id=user_id,
        text=text,
        reply_markup=kb)
    return msg.message_id
async def dropinlinekeyboard(
    user_id: int,
    buttons: list[str],
    text: str = ""):

    keyboard = [
        [
            InlineKeyboardButton(
                text=b,
                callback_data=f"btn:{b}"
            )
            for b in buttons[i:i + 4]
        ]
        for i in range(0, len(buttons), 4)
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=keyboard)

    msg = await safe_send(bot.send_message,
        chat_id=user_id,
        text=text,
        reply_markup=kb)
    return msg.message_id

async def edit_text(chat_id: int, message_id: int, text: str):
    await safe_send(
        bot.edit_message_text,
        chat_id=chat_id,
        message_id=message_id,
        text=text
    )

async def edit_inlinekeyboard(chat_id, message_id, buttons):
    if buttons:
        keyboard = [
                [
                    InlineKeyboardButton(
                        text=b,
                        callback_data=f"btn:{b}"
                    )
                    for b in buttons[i:i + 4]
                ]
                for i in range(0, len(buttons), 4)
            ]

        kb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    else:
        kb = None
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=kb)