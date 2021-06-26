from subscribers.models import Subscriber
from telegram_bot.commands import static_text
import telegram

from django.conf import settings
from telegram_bot.models import User
from telegram import MessageEntity


def get_profile_by_phone_number(phone):
    ps = Subscriber.objects.filter(phone=phone)
    text = ''
    profile_data = []
    if ps.exists():
        if ps.count() > 1:
            text += static_text.is_more_than_one_profiles.format(phone=phone)
            for p in ps:
                profile_data.append(p)
            return profile_data, text
        else:
            text += static_text.is_one_profile.format(phone=phone)
            for p in ps:
                profile_data.append(p)
            return profile_data, text
    else:
        text += static_text.is_no_one_profile.format(phone=phone)
    return None, text


# def send_typing_action(func):
#     """Sends typing action while processing func command."""
#
#     @wraps(func)
#     def command_func(update, context, *args, **kwargs):
#         context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=telegram.ChatAction.TYPING)
#         return func(update, context, *args, **kwargs)
#
#     return command_func


def send_message(user_id, text, parse_mode=None, reply_markup=None, reply_to_message_id=None,
                 disable_web_page_preview=None, entities=None, tg_token=settings.TELEGRAM_BOT_TOKEN):
    bot = telegram.Bot(tg_token)
    try:
        if entities:
            entities = [
                MessageEntity(type=entity['type'],
                              offset=entity['offset'],
                              length=entity['length']
                              )
                for entity in entities
            ]

        m = bot.send_message(
            chat_id=user_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
            reply_to_message_id=reply_to_message_id,
            disable_web_page_preview=disable_web_page_preview,
            entities=entities,
        )
    except telegram.error.Unauthorized:
        print(f"Can't send message to {user_id}. Reason: Bot was stopped.")
        User.objects.filter(user_id=user_id).update(is_blocked_bot=True)
        success = False
    except Exception as e:
        print(f"Can't send message to {user_id}. Reason: {e}")
        success = False
    else:
        success = True
        User.objects.filter(user_id=user_id).update(is_blocked_bot=False)
    return success
