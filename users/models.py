from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_agent = models.CharField(max_length=128, verbose_name='User Agent')
    ip_address = models.CharField(max_length=128, verbose_name='IP Address')

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'