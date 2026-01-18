from bot import dp
from program import program 
from aiogram import F
from aiogram.types import Message

@dp.message(F.text.startswith("/start"))
async def command_handler(message: Message):
    await program.commands(message)

@dp.message(F.audio)
async def audio_handler(message: Message):
    await program.message(message)
@dp.message(F.text)
async def text_handler(message: Message):
    await program.message(message)
@dp.message(F.voice)
async def voice_handler(message: Message):
    await program.message(message)
@dp.message(F.video_note)
async def handle_video_note(message: Message):
    await program.message(message)
@dp.message(F.photo)
async def photo_handler(message: Message):
    await program.message(message)
@dp.message(F.animation)
async def animation_handler(message: Message):
    await program.message(message)
@dp.message(F.sticker)
async def sticker_handler(message: Message):
    await program.message(message)
