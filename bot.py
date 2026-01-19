from aiogram import Bot
from config import key
from aiogram import Dispatcher
from aiogram import Router

rt = Router()
dp = Dispatcher()
dp.include_router(rt)
bot = Bot(token=key)
print('SANDBOX BOT')