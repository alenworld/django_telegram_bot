import logging

from django.conf import settings
from telegram import Update
from telegram import ReplyKeyboardRemove
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from telegram_bot.utils.misc import send_message
from telegram_bot.keyboard.default import getCity, getPhone
from telegram_bot.keyboard.default.menus import menu
from telegram_bot.models import Claim, User

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
CITY_CLAIM, ADDRESS_CLAIM, PHONE_CLAIM = range(3)


def claim(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.username)
    update.message.reply_text('Ваше місто?', reply_markup=getCity)

    return CITY_CLAIM


def city_claim(update: Update, context: CallbackContext) -> int:
    # Get city name
    context.user_data[CITY_CLAIM] = update.message.text
    logger.info(f'user_data: {context.user_data}')
    # Ask address
    update.message.reply_text('Вкажіть вашу адресу:', reply_markup=ReplyKeyboardRemove())

    return ADDRESS_CLAIM


def address_claim(update: Update, context: CallbackContext) -> int:
    # Get address
    context.user_data[ADDRESS_CLAIM] = update.message.text
    logger.info(f'user_data: {context.user_data}')
    # Ask phone number
    update.message.reply_text('Адресу отримано.\n Поділіться номером для  зв`язку:', reply_markup=getPhone)

    return PHONE_CLAIM


def phone_claim(update: Update, context: CallbackContext) -> int:
    # Get phone number
    context.user_data[PHONE_CLAIM] = update.message.contact.phone_number
    logger.info(f'user_data: {context.user_data}')
    # Info to database
    user_data = context.user_data
    u, context = User.get_user_and_created(update, context)
    c = Claim(
        sender=u,
        city=user_data[CITY_CLAIM],
        address=user_data[ADDRESS_CLAIM],
        phone=user_data[PHONE_CLAIM]
    )
    c.save()

    # Finish claim states
    update.message.reply_text('Заявка прийнята.', reply_markup=menu)
    # Send to admins group
    send_message(user_id=settings.TELEGRAM_BOT_CHANNEL,
                             text=f'Місто: {user_data[CITY_CLAIM]}\nАдреса: {user_data[ADDRESS_CLAIM]}\nНомер: {user_data[PHONE_CLAIM]}', parse_mode='HTML')
    #

    return ConversationHandler.END


def cancel_claim(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Заявку скасовано.\nПочаткове меню:', reply_markup=menu
    )
    return ConversationHandler.END
