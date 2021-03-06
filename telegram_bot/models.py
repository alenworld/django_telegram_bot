from django.db import models
from django.utils import timezone
from .utils.extract_data import extract_user_data_from_update


class User(models.Model):
    user_id = models.IntegerField(
        verbose_name='Telegram User ID',
        primary_key=True
    )
    username = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='Telegram Username',
        unique=True
    )
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    language_code = models.CharField(max_length=2, default='uk', blank=True, help_text="Telegram client's lang")
    notification = models.BooleanField(default=True)
    phone = models.CharField(max_length=13, blank=True, null=True)

    is_blocked_bot = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)

    login = models.CharField(max_length=32, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    joined = models.DateTimeField(auto_now_add=True)

    # json = models.JSONField(null=True, default=None)

    class Meta:
        ordering = ['-joined']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    @classmethod
    def get_user_and_created(cls, update, context):
        """ python-telegram-bot's Update, Context --> User instance """
        data = extract_user_data_from_update(update)
        u, created = cls.objects.update_or_create(user_id=data["user_id"], defaults=data)

        return u, created

    @classmethod
    def get_user(cls, update, context):
        u, _ = cls.get_user_and_created(update, context)
        return u

    @classmethod
    def get_user_by_username_or_user_id(cls, string):
        """ Search user in DB, return User or None if not found """
        username = str(string).replace("@", "").strip().lower()
        if username.isdigit():  # user_id
            return cls.objects.filter(user_id=int(username)).first()
        return cls.objects.filter(username__iexact=username).first()


class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пользователь: {self.user}, выполнил действие: {self.action}, время {self.created_at.strftime('(%H:%M, %d %B %Y)')}"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField(max_length=4096)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение {self.pk} от {self.sender}'


class Claim(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    city = models.CharField(max_length=36, null=True)
    address = models.TextField(max_length=100, null=True)
    phone = models.CharField(max_length=13, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Заявка на подключения"
        verbose_name_plural = 'Заявки на подключения'

    def __str__(self):
        return f'Заявка #{self.pk} от {self.sender}'
