from django.utils import timezone

from django.conf import settings
from telegram_bot.models import User, UserActionLog


def handler_logging(action_name=None):
    """ Turn on this decorator via ENABLE_DECORATOR_LOGGING variable in config.settings """

    def decor(func):
        def handler(update, context, *args, **kwargs):
            user, _ = User.get_user_and_created(update, context)
            action = f"{func.__module__}.{func.__name__}" if not action_name else action_name
            UserActionLog.objects.create(user_id=user.user_id, action=action, created_at=timezone.now())
            return func(update, context, *args, **kwargs)

        return handler if settings.ENABLE_DECORATOR_LOGGING else func

    return decor
