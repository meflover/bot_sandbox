from bot import bot
import time
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class RateLimiter:
    def __init__(self, limit=30, interval=1.0):
        self.score = 0
        self.limit = limit
        self.interval = interval

    def acquire(self):
        while self.score >= self.limit:
            time.sleep(self.interval)
            self.score = 0
        self.score += 1
limiter = RateLimiter()


async def safe_send(send_func, *args, **kwargs):
    try:
        limiter.acquire()
        result = await send_func(*args, **kwargs)
        print(f"[SAFE_SEND] {send_func.__name__}: {limiter.score}")
        return result
    except Exception as e:
        print(f"[ERROR] safe_send: {e}\n{args}\n{send_func}")
        return None


async def answer(id_, text):
    await safe_send(bot.send_message,id_,text)
async def reply(message, text):
    await safe_send(message.reply, text)


async def dropvoice(user_id, file_id):
    await safe_send(bot.send_voice, user_id, file_id)

async def drop_video_note(user_id, file_id):
    await safe_send(bot.send_video_note, user_id, file_id)

async def dropaudio(user_id, file_id):
    await safe_send(bot.send_audio, user_id, file_id)
async def dropsticker(user_id, file_id):
    await safe_send(bot.send_sticker, user_id, file_id)
async def dropgif(user_id, file_id):
    await safe_send(bot.send_animation, user_id, file_id)

async def dropmedia(user_id, media):
    await safe_send(bot.send_media_group, user_id, media)
async def dropphoto_html(user_id, photo_id, text =''):
    await safe_send(bot.send_photo, user_id, photo_id, caption=text, parse_mode='HTML')

async def dropphoto(user_id, photo_id, text=''):
    await safe_send(bot.send_photo, user_id, photo_id, caption=text)
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

    await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=kb
    )

