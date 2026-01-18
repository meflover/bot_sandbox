from config import admin_id
from classes import session
from handlers.safesend import *
from aiogram.types import Message

class Editor:
    def __init__(self):
        self.admin_id = admin_id

    @staticmethod
    async def commands(message: Message):
        parts = message.text.split(maxsplit=1)
        if parts[0] == '/start':
            text = "Hello World!"
            await reply(message,text)

    @staticmethod
    async def message(message: Message):

        user = session.short_init(message.from_user.id)

        username = message.from_user.username

        if user.status == 'ban':
            await reply(message,'You blocked.')
            return

        text = message.text if message.text is not None else ''
        caption = message.caption if message.caption is not None else ''

        t_ = text + caption

        if message.text:
            await answer(user.id, t_)
            await dropkeyboard(user.id, True, ["1","2","3","4","5"], t_)
        if message.audio:
            file_id = message.audio.file_id
            await dropaudio(user.id, file_id)
        if message.photo:
            photo = max(message.photo, key=lambda x: x.height)
            file_id = photo.file_id
            await dropphoto(user.id, file_id, t_)
        if message.video_note:
            file_id = message.video_note.file_id
            await dropkrug(user.id, file_id)
        if message.voice:
            file_id = message.voice.file_id
            await dropvoice(user.id, file_id)
        if message.animation:
            file_id = message.animation.file_id
            await dropgif(user.id, file_id)
        if message.sticker:
            file_id = message.sticker.file_id
            await dropsticker(user.id, file_id)


program = Editor()