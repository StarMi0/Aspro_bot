from aiogram import types, Dispatcher
from bot_create import dp, bot
from keyboard.kb import starting_kb


async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name

    await message.answer(f"Приветствую, {user_name}! \nВоспользуйтесь кнопками ниже, чтобы ввести необходимые данные.",
                         reply_markup=starting_kb)


if __name__ == "__main__":
    pass
