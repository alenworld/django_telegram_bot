from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from telegram_bot.utils.misc import send_message
from telegram_bot.commands.base_commands import unknown
from telegram_bot.keyboard.default.menus import menu
from telegram_bot.keyboard.default.utils import getUsersList
from telegram_bot.models import User

TEXT, USER_LIST = range(2)


def admin_help(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    # if User is Admin
    if User.objects.get(user_id=user_id).is_admin:
        update.message.reply_text(
            text='Довідка адміністратора.\n'
                 'Команди:\n'
                 '/mailing_message - Відправлення повідомлення користувачам бота'
        )
    else:
        # if User not Admin call unknown command
        unknown(update, context)


def mailing_message(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    # if User is Admin
    if User.objects.get(user_id=user_id).is_admin:
        update.message.reply_text(text='Пришлите текст рассылки', reply_markup=ReplyKeyboardRemove())
        return TEXT
    else:
        # if User not Admin call unknown command
        unknown(update, context)
        return ConversationHandler.END


def text_message(update: Update, context: CallbackContext) -> int:
    # Get text message
    context.user_data[TEXT] = update.message.text
    # Ask received user list
    update.message.reply_text('Кому разослать сообщение?:', reply_markup=getUsersList)

    return USER_LIST


def mailing_start(update: Update, context: CallbackContext) -> int:
    context.user_data[USER_LIST] = update.message.text
    users_received = context.user_data[USER_LIST]
    text = context.user_data[TEXT]

    if users_received == 'All':
        users = User.objects.all()
    elif users_received == 'Only subs':
        users = User.objects.filter(is_subscriber=True)
    elif users_received == 'No subs':
        users = User.objects.filter(is_subscriber=False)
    count = 0
    for user in users:
        user_id = user.user_id
        if send_message(user_id=user_id, text=text):
            count += 1
        else:
            pass

    update.message.reply_text(text=f'Рассылка завершена! Получили сообщение: {count}', reply_markup=menu)
    return ConversationHandler.END


def cancel_mailing(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Рассылка отменена.\nПочаткове меню:', reply_markup=menu
    )
    return ConversationHandler.END
