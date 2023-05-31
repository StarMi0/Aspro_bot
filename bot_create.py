import asyncio

from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from func.functions import key_dict

# Connect to Telegramm API
bot = Bot(token=key_dict['BOT_key'])
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_):
    # asyncio.create_task(run_vk())
    print('Telegram bot is online')


if __name__ == "__main__":
    pass
