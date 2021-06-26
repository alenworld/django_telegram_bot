import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.models import User
from subscribers.models import Subscriber
from telegram_bot.keyboard.default import menus
from telegram_bot.keyboard.inline import financial_operations

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Subscriber information
def user_info(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)

    text = f'👤 Логін: {user.login}\n' \
           f'💰 Баланс: {subscriber.deposit}\n' \
           f'💼 Грошовий рахунок: {subscriber.financial_account}\n' \
           f'🖋 ПІБ: {subscriber.name}\n' \
           f'🏠 Адреса: {subscriber.street} {subscriber.build} кв.{subscriber.apartment}\n' \
           f'🗓 Дата підключення: {subscriber.registration}'
    update.message.reply_text(text, reply_markup=menus.user_menu)


# Subscriber tariff plan information
def tariff_plan(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)

    text = f'👤 Тариф: Службовий\n' \
           f'💰 Абонплата: 0 грн/міс\n' \
           f'💼 Статичний IP: Ні\n'
    update.message.reply_text(text, reply_markup=menus.user_menu)


# Subscriber TV tariff plan information
def tv_tariff_plan(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)

    text = f'👤 Тариф: Максимальний+Кіно\n' \
           f'💰 Абонплата: 159 грн/міс\n' \
           f'💼 Кількість каналів: ~250\n' \
           f'💼 Кінозал: Активовано\n'
    update.message.reply_text(text, reply_markup=menus.user_menu)


# Subscriber's last financial operation info
# Inline keyboard buttons: Payments, Withdraw
def financial_operations_info(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)
    keyboard = financial_operations.financial_operations_keyboard('all_financial_operations')
    text = 'Оберіть розділ фінансових операцій'
    update.message.reply_text(text, reply_markup=keyboard)


# Subscriber's last financial operation info
# Inline keyboard buttons: Payments, Withdraw
# Calling this function from inline mode
def all_financial_operations_info(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # user_id = update.callback_query.from_user.id
    # user = User.objects.get(user_id=user_id)
    # subscriber = Subscriber.objects.get(login=user.login)
    text = 'Оберіть розділ фінансових операцій'
    keyboard = financial_operations.financial_operations_keyboard('all_financial_operations')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def payments_info(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user_id = update.callback_query.from_user.id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)
    text = f'Дата\t\tОпис\tСума\tДепозит до\t\n' \
           f'2021-02-17\tPrivat24\t180.00\t0.00\t\n' \
           f'2021-02-17\tiBox\t180.00\t0.00\t\n' \
           f'2021-02-17\tMonobank\t180.00\t0.00\t\n' \
           f'2021-02-17\tPrivat24\t180.00\t0.00\t\n'
    keyboard = financial_operations.financial_operations_keyboard('return_back_finance')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)


def withdraw_info(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user_id = update.callback_query.from_user.id
    user = User.objects.get(user_id=user_id)
    subscriber = Subscriber.objects.get(login=user.login)
    text = f'Дата\t\tОпис\tСума\tДепозит\t\n' \
           f'2021-02-17\t\tАктивація т..\t420.00\t-420.00\t\n' \
           f'2021-02-17\t\tiBox\t180.00\t0.00\t\n' \
           f'2021-02-17\t\tMonobank\t180.00\t0.00\t\n' \
           f'2021-02-17\t\tPrivat24\t180.00\t0.00\t\n'
    keyboard = financial_operations.financial_operations_keyboard('return_back_finance')
    query.edit_message_text(text, parse_mode='HTML', reply_markup=keyboard)
