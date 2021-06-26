import logging
from telegram import Update
from telegram import ReplyKeyboardRemove
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from telegram_bot.keyboard.inline import make_addresses_inline_keyboard
from telegram_bot.models import User
from telegram_bot.utils.misc import get_profile_by_phone_number
from telegram_bot.keyboard.default.utils import getPhone
from telegram_bot.keyboard.default.menus import menu, user_menu
from telegram_bot.commands import static_text

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
PHONE, ADDRESS = range(2)


def auth(update: Update, _: CallbackContext) -> int:
    text = ''
    user = update.message.from_user
    user = User.objects.get(user_id=user.id)
    if user.is_subscriber:
        text += static_text.authorization_true
        update.message.reply_text(text, parse_mode='HTML', reply_markup=user_menu)
        return ConversationHandler.END
    else:
        text += static_text.share_phone_number
        logger.info("User %s started the conversation.", user.username)

        update.message.reply_text(text, parse_mode='HTML',
                                  reply_markup=getPhone,
                                  )
        return PHONE


def phone(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    phone_number = update.message.contact.phone_number
    messageUserID = user.id
    contactUserID = update.message.contact.user_id

    logger.info("Phone of %s: %s", user.first_name, phone_number)

    check_phone = f'🔄 Номер Вашого мобільного отримано. Перевіряємо...\n'
    update.message.reply_text(check_phone, parse_mode='HTML')
    update.message.reply_chat_action(action='typing', timeout=4.0)

    if messageUserID != contactUserID:
        update.message.reply_text(
            text=f'❌ Відмовленно в авторизації.\n👉 Отриманий номер не пов\'язан з Вашим аккаунтом'
                 f' Telegram.\n ',
            parse_mode='HTML', reply_markup=menu,
        )
        return ConversationHandler.END
    elif messageUserID == contactUserID:
        update.message.reply_text(
            text=f'✅ Ваш номер перевірено!',
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove()
        )
    logger.info("Checked %s: %s", user.first_name, phone_number)
    # Update field "phone" for telegram user
    User.objects.filter(user_id=user.id).update(phone=phone_number)

    # Reply keyboard with 1 or more addresses
    p, text = get_profile_by_phone_number(phone_number)

    if p is not None:
        keyboard = make_addresses_inline_keyboard(p)
        update.message.reply_text(text=text, parse_mode='HTML', reply_markup=keyboard)
        return ADDRESS
    else:
        # ЮЗЕР ДЛЯ ТЕСТА МЕНЮ АБОНЕНТОВ
        # text = 'Тестування меню абонентiв'
        # testphone = '00000000000'
        # p, _ = get_profile_by_phone_number(testphone)1
        # keyboard = make_addresses_inline_keyboard(p)

        text += 'Скористайтесь довідкою /help або протестуйте меню.'
        update.message.reply_text(text=text, parse_mode='HTML', reply_markup=menu)
        return ConversationHandler.END
    return ConversationHandler.END


def address(update: Update, _: CallbackContext) -> int:
    update.callback_query.edit_message_text(text=static_text.authorization_complete, parse_mode='HTML')
    query = update.callback_query
    login = query.data
    user = query.from_user

    # update.message.reply_text(text=text, parse_mode='HTML', reply_markup=user_menu)
    # query.edit_message_text(text=text, parse_mode='HTML')
    # Update Telegram User Data
    User.objects.filter(user_id=user.id).update(login=login, is_subscriber=True)
    update.callback_query.message.reply_text(text='👋', parse_mode='HTML', reply_markup=user_menu)

    return ConversationHandler.END


def cancel(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user.id
    update.message.reply_text(
        'Авторизацію скасовано.\nПочаткове меню:', reply_markup=menu
    )
    return ConversationHandler.END
