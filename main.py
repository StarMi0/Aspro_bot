from aiogram import executor
from bot_create import on_startup, dp, bot

bot.register_handler_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
