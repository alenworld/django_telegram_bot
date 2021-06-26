from django.conf import settings

from telegram import Bot
from telegram.ext import (
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    ConversationHandler
)

from .commands.menu import (
    claim, chat_support, auth, faq, personal_account
)
from .commands.menu.auth import PHONE, ADDRESS, phone, cancel, address
from .commands.menu.claim import CITY_CLAIM, ADDRESS_CLAIM, cancel_claim, address_claim, city_claim, phone_claim, \
    PHONE_CLAIM
from .commands import base_commands
from .commands import admin_commands
from .commands.admin_commands import TEXT, USER_LIST

BACK = 'back'


def setup():
    tgbot = Bot(settings.TELEGRAM_BOT_TOKEN)
    if settings.TELEGRAM_BOT_WEBHOOK_ENABLED:
        tgbot.set_webhook(
            settings.TELEGRAM_BOT_WEBHOOK_URL + settings.TELEGRAM_BOT_WEBHOOK_PATH
        )

    dp = Dispatcher(tgbot, None)

    # Authorization
    conv_handler_auth = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('👤 Особистий кабінет'), auth)],
        states={
            PHONE: [MessageHandler(Filters.contact, phone)],
            ADDRESS: [CallbackQueryHandler(address)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Claim
    conv_handler_claim = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('🔌 Заявка на підключення'), claim)],
        states={
            CITY_CLAIM: [
                MessageHandler(Filters.text(['📍 Кропивницький', '📍 Знам`янка']), city_claim, pass_user_data=True)],
            ADDRESS_CLAIM: [MessageHandler(Filters.all, address_claim, pass_user_data=True)],
            PHONE_CLAIM: [MessageHandler(Filters.contact, phone_claim, pass_user_data=True)],
        },
        fallbacks=[CommandHandler('cancel', cancel_claim)],
    )

    # Mailing to bot users
    conv_handler_mailing = ConversationHandler(
        entry_points=[CommandHandler('mailing_message', admin_commands.mailing_message)],
        states={
            TEXT: [MessageHandler(Filters.all, admin_commands.text_message, pass_user_data=True)],
            USER_LIST: [MessageHandler(Filters.all, admin_commands.mailing_start, pass_user_data=True)],
        },
        fallbacks=[CommandHandler('cancel', admin_commands.cancel_mailing)],
    )

    # HANDLERS ADD -------------------------
    # Base commands
    dp.add_handler(CommandHandler('start', base_commands.command_start))
    dp.add_handler(CommandHandler('help', base_commands.command_help))

    # Conversations
    dp.add_handler(conv_handler_auth)  # Authorization
    dp.add_handler(conv_handler_claim)  # Claims
    # admin commands
    dp.add_handler(CommandHandler('admin', admin_commands.admin_help))
    dp.add_handler(conv_handler_mailing)  # Mailing to all bot users

    # FAQ
    dp.add_handler(CommandHandler('faq', faq))
    dp.add_handler(MessageHandler(Filters.regex('💡 F.A.Q'), faq))
    dp.add_handler(CallbackQueryHandler(base_commands.inline_button))  # pattern='main'

    dp.add_handler(MessageHandler(Filters.regex('✉️ Чат з оператором'), chat_support))

    # User menu
    dp.add_handler(MessageHandler(Filters.regex('👁 Інформація про користувача'), personal_account.user_info))
    dp.add_handler(MessageHandler(Filters.regex('🌐 Мій тариф'), personal_account.tariff_plan))
    dp.add_handler(MessageHandler(Filters.regex('📺 Телебачення'), personal_account.tv_tariff_plan))
    dp.add_handler(MessageHandler(Filters.regex('💳 Фінансові операції'), personal_account.financial_operations_info))

    # dp.add_handler(MessageHandler(Filters.all, base_commands.unknown))
    dp.add_error_handler(base_commands.error_handler)
    # ------------------------------------
    return tgbot, dp


bot, dispatcher = setup()
