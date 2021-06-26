from django.urls import path
from django.conf import settings
from .views import UpdateHandler
from . import views


urlpatterns = [
    path('webhook/', UpdateHandler.as_view(), name='update_handler_url'),
]
