import asyncio

from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN
from app.handlers.commands import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    print("ربات روشن شد!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())