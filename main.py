import asyncio
import logging
from os import name as os_name

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import BotSettings

from handlers import default_handlers, user_handlers, other_handlers


async def main():
    logging.basicConfig(level=logging.DEBUG)
    botconfig = BotSettings.load_from_file('.keys/.env')

    storage = MemoryStorage()

    bot = Bot(token=botconfig.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    
    dp.include_router(default_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        if os_name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
    