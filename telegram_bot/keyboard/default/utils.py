from telegram import ReplyKeyboardMarkup, KeyboardButton

getPhone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Поділитися номером телефону',
                           request_contact=True)
        ],
    ],
)

getCity = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📍 Кропивницький'),
            KeyboardButton(text='📍 Знам`янка')
        ],
    ],
    resize_keyboard=True
)

getUsersList = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='All'),
            KeyboardButton(text='Only subs')
        ],
[
            KeyboardButton(text='No subs')
        ],
    ],
    resize_keyboard=True
)