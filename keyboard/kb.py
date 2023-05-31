from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def starting_kb():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Поступление', callback_data='receiving'),
         InlineKeyboardButton(text='Расход', callback_data='expense')],
        [InlineKeyboardButton(text='Трансфер', callback_data='transfer')]
    ],
        resize_keyboard=True)
    return markup


if __name__ == "__main__":
    pass
