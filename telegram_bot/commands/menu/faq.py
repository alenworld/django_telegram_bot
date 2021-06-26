from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from telegram_bot.keyboard.inline.faq import make_faq_inline_keyboard, make_faq_button_answer
from telegram_bot.utils import faq_answers

MsgFAQ = '💡<b>FAQ</b>'


def faq(update: Update, context: CallbackContext):
    """Send message on `/faq`."""
    # Get user that sent /faq and log his name
    user = update.message.from_user
    keyboard = make_faq_inline_keyboard('main')
    update.message.reply_text(text=MsgFAQ, parse_mode='HTML', reply_markup=keyboard)


def faq_menu(update: Update, context: CallbackContext):
    """Prompt same text & keyboard as `faq` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    query.answer()
    keyboard = make_faq_inline_keyboard('main')
    query.edit_message_text(text=MsgFAQ, parse_mode='HTML', reply_markup=keyboard)


def general(update: Update, context: CallbackContext):
    """Show buttons Category: General """
    query = update.callback_query
    query.answer()
    text = MsgFAQ + '\n ↘️<u>Загальні питання</u>\n'
    keyboard = make_faq_inline_keyboard('general')
    query.edit_message_text(text=text, parse_mode='HTML', reply_markup=keyboard)


def connect(update: Update, context: CallbackContext):
    """Show buttons Category: Connect """
    query = update.callback_query
    query.answer()
    text = MsgFAQ + '\n ↘️<u>Підключення</u>\n'
    keyboard = make_faq_inline_keyboard('connect')
    query.edit_message_text(text=text, parse_mode='HTML', reply_markup=keyboard)


def internet(update: Update, context: CallbackContext):
    """Show buttons Category: Internet """
    query = update.callback_query
    query.answer()
    text = MsgFAQ + '\n ↘️<u>Інтернет</u>\n'
    keyboard = make_faq_inline_keyboard('internet')
    query.edit_message_text(text=text, parse_mode='HTML', reply_markup=keyboard)


def tv(update: Update, context: CallbackContext):
    """Show buttons Category: Digital Television """
    query = update.callback_query
    query.answer()
    text = MsgFAQ + '\n ↘️<u>Цифрове телебачення</u>\n'
    keyboard = make_faq_inline_keyboard('tv')
    query.edit_message_text(text=text, parse_mode='HTML', reply_markup=keyboard)


def payment(update: Update, context: CallbackContext):
    """Show buttons Category: Payment """
    query = update.callback_query
    query.answer()
    text = MsgFAQ + '\n ↘️<u>Оплата</u>\n'
    keyboard = make_faq_inline_keyboard('payment')
    query.edit_message_text(text=text, parse_mode='HTML', reply_markup=keyboard)



def general_answers(update: Update, context: CallbackContext):
    """Show answers general"""
    query = update.callback_query
    query.answer()
    text = ''
    data = query.data[:-2:-1]
    text += MsgFAQ + ' ➡️Загальні питання\n\n'
    if data == '1':
        text += faq_answers.g1_1
    elif data == '2':
        text += faq_answers.g1_2
    elif data == '3':
        text += faq_answers.g1_3
    elif data == '4':
        text += faq_answers.g1_4
    elif data == '5':
        text += faq_answers.g1_5
    elif data == '6':
        text += faq_answers.g1_6
    elif data == '7':
        text += faq_answers.g1_7
    elif data == '8':
        text += faq_answers.g1_8

    keyboard = make_faq_button_answer('g')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def connect_answers(update: Update, context: CallbackContext):
    """Show answers connect"""
    query = update.callback_query
    query.answer()
    text = ''
    data = query.data[:-2:-1]
    text += MsgFAQ + ' ➡️Підключення\n\n'
    if data == '1':
        text += faq_answers.c1_1
    elif data == '2':
        text += faq_answers.c1_2
    elif data == '3':
        text += faq_answers.c1_3
    elif data == '4':
        text += faq_answers.c1_4
    elif data == '5':
        text += faq_answers.c1_5
    elif data == '6':
        text += faq_answers.c1_6
    elif data == '7':
        text += faq_answers.c1_7
    elif data == '8':
        text += faq_answers.c1_8

    keyboard = make_faq_button_answer('c')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def internet_answers(update: Update, context: CallbackContext):
    """Show answers internet"""
    query = update.callback_query
    query.answer()
    text = ''
    data = query.data[:-2:-1]
    text += MsgFAQ + ' ➡️Інтернет\n\n'
    if data == '1':
        text += faq_answers.i1_1
    elif data == '2':
        text += faq_answers.i1_2
    elif data == '3':
        text += faq_answers.i1_3
    elif data == '4':
        text += faq_answers.i1_4
    elif data == '5':
        text += faq_answers.i1_5
    elif data == '6':
        text += faq_answers.i1_6
    elif data == '7':
        text += faq_answers.i1_7
    elif data == '8':
        text += faq_answers.i1_8

    keyboard = make_faq_button_answer('i')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def tv_answers(update: Update, context: CallbackContext):
    """Show answers tv"""
    query = update.callback_query
    query.answer()
    text = ''
    data = query.data[:-2:-1]
    text += MsgFAQ + ' ➡️Цифрове телебачення\n\n'
    if data == '1':
        text += faq_answers.t1_1
    elif data == '2':
        text += faq_answers.t1_2
    elif data == '3':
        text += faq_answers.t1_3
    elif data == '4':
        text += faq_answers.t1_4
    elif data == '5':
        text += faq_answers.t1_5
    elif data == '6':
        text += faq_answers.t1_6
    elif data == '7':
        text += faq_answers.t1_7
    elif data == '8':
        text += faq_answers.t1_8

    keyboard = make_faq_button_answer('t')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def payment_answers(update: Update, context: CallbackContext):
    """Show answers payment"""
    query = update.callback_query
    query.answer()
    text = ''
    data = query.data[:-2:-1]
    text += MsgFAQ + ' ➡️Оплата\n\n'
    if data == '1':
        text += faq_answers.p1_1
    elif data == '2':
        text += faq_answers.p1_2
    elif data == '3':
        text += faq_answers.p1_3
    elif data == '4':
        text += faq_answers.p1_4
    elif data == '5':
        text += faq_answers.p1_5
    elif data == '6':
        text += faq_answers.p1_6
    elif data == '7':
        text += faq_answers.p1_7
    elif data == '8':
        text += faq_answers.p1_8

    keyboard = make_faq_button_answer('p')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def thanks(update: Update, context: CallbackContext):
    """
    if user getting answer
    """
    query = update.callback_query
    query.answer()
    text = '✅ Приємно було допомогти.\nЗнайти відповідь на питання - /faq\nДовідка бота - /help'
    query.edit_message_text(text=text, parse_mode='HTML')
