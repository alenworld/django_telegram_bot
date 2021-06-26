import logging
import html
import json
import traceback
from django.conf import settings
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from telegram_bot.commands import static_text
from telegram_bot.keyboard.default import menus
from telegram_bot.models import User, Message

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

DEVELOPER_CHAT_ID = settings.TELEGRAM_BOT_CHANNEL_DEV


def command_start(update: Update, context: CallbackContext):
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.start_created.format(first_name=u.first_name)
    else:
        text = static_text.start_not_created.format(first_name=u.first_name)

    update.message.reply_text(text=text,
                              reply_markup=menus.menu)


def command_help(update: Update, context: CallbackContext):
    update.message.reply_text(text=static_text.help_info, reply_markup=menus.menu)


def inline_button(update: Update, context: CallbackContext):
    """Callback method handling buttons press"""
    query = update.callback_query
    if query.data == 'main':
        faq_menu(update, context)
    elif query.data == 'g':
        general(update, context)
    elif query.data == 'c':
        connect(update, context)
    elif query.data == 'i':
        internet(update, context)
    elif query.data == 't':
        tv(update, context)
    elif query.data == 'p':
        payment(update, context)
    elif query.data[:2:] == 'g1':
        general_answers(update, context)
    elif query.data[:2:] == 'c1':
        connect_answers(update, context)
    elif query.data[:2:] == 'i1':
        internet_answers(update, context)
    elif query.data[:2:] == 't1':
        tv_answers(update, context)
    elif query.data[:2:] == 'p1':
        payment_answers(update, context)
    elif query.data == 'thank':
        thanks(update, context)
    elif query.data == 'fpayments':
        payments_info(update, context)
    elif query.data == 'fwithdraws':
        withdraw_info(update, context)
    elif query.data == 'all_financial_operations':
        all_financial_operations_info(update, context)


def error_handler(update: object, context: CallbackContext) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = ''.join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f'An exception was raised while handling an update\n'
        f'<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}'
        '</pre>\n\n'
        f'<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n'
        f'<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n'
        f'<pre>{html.escape(tb_string)}</pre>'
    )

    # Finally, send the message
    context.bot.send_message(chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML)


# def bad_command(update: Update, context: CallbackContext) -> None:
#     """Raise an error to trigger the error handler."""
#     context.bot.wrong_method_name()  # type: ignore[attr-defined]


def unknown(update: Update, context: CallbackContext):
    chat_id = update.message.from_user.id
    text = update.message.text

    u, created = User.get_user_and_created(update, context)

    m = Message(
        sender=u,
        text=text
    )
    m.save()

    reply_text = f'Ваш ID = {chat_id}\n{text}\n'
    reply_text += static_text.unknown_command_info
    update.message.reply_text(
        text=reply_text, parse_mode='HTML'
    )
