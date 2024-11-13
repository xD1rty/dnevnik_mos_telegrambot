import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers.user_handlers import user_router

async def start():
    bot = Bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_router(user_router)

    try:
        await dp.start_polling(bot)
    except:
        print("Error.") # TODO: logging
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
