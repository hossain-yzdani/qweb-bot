from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💻 درباره ما"),
            KeyboardButton(text="📞 تماس با ما"),
        ],
        [
            KeyboardButton(text="💡 دریافت مشاوره"),
            KeyboardButton(text="🛠 خدمات ما"),
        ],
    ],
    resize_keyboard=True
)