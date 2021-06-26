from django.contrib import admin

from .models import User, Message, Claim


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'phone', 'joined', 'updated_at')
    list_display_links = ('user_id', 'username')
    list_filter = ["is_blocked_bot", "is_moderator"]
    search_fields = ('user_id', 'username')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text', 'date')
    list_display_links = ('sender', 'text')
    search_fields = ('sender', 'text')


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sender', 'city', 'address', 'phone', 'date')
    search_fields = ('sender', 'city', 'phone', 'date')
