from datetime import date
from django.db import models


class Subscriber(models.Model):
    """Абонент"""
    login = models.CharField(max_length=36, unique=True)
    password = models.CharField(max_length=36, null=True, blank=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    street = models.CharField(max_length=100, null=True, blank=True)
    build = models.CharField(max_length=36, null=True, blank=True)
    apartment = models.CharField(max_length=36, null=True, blank=True)

    financial_account = models.IntegerField(auto_created=True, unique=True, null=True, blank=True)
    deposit = models.IntegerField(default=0.00)
    registration = models.DateField(default=date.today)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Абонент'
        verbose_name_plural = 'Абоненты'
