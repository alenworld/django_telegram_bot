from telegram import ReplyKeyboardMarkup, KeyboardButton

user_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='👁 Інформація про користувача'),
            KeyboardButton(text='💳 Фінансові операції')
        ],
        [
            KeyboardButton(text='📺 Телебачення'),
            KeyboardButton(text='🌐 Мій тариф')
        ],
        [
            KeyboardButton(text='💡 F.A.Q'),
            KeyboardButton(text='🛠 Підтримка')
        ],
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='🔌 Заявка на підключення'),
            KeyboardButton(text='👤 Особистий кабінет')
        ],
        [

            KeyboardButton(text='💡 F.A.Q'),
            KeyboardButton(text='✉️ Чат з оператором')
        ]
    ],
    resize_keyboard=True
)
