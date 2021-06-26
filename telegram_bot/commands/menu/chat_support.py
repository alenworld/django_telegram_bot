from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.keyboard.default.menus import menu


def chat_support(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    update.message.reply_text('Функція в розробці.', reply_markup=menu)
