import asyncio
from bot import bot,dp
from handlers import inputs 

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e) 