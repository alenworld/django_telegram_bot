from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'login', 'phone', 'registration')
    list_display_links = ('pk', 'login')
    search_fields = ('login', 'phone')
