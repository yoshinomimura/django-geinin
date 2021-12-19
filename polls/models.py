from django.db import models


class Poll(models.Model):
    is_funny = models.BooleanField(default=True, verbose_name='面白い')
    comedian = models.ForeignKey('comedians.Comedian', on_delete=models.CASCADE, related_name='polls', verbose_name='芸人')
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='polls', verbose_name='ユーザー')
    user_agent = models.CharField(max_length=128, blank=True, verbose_name='User Agent')
    ip_address = models.CharField(max_length=128, blank=True, verbose_name='IP Address')
    created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新日')

    class Meta:
        verbose_name = '投票'
        verbose_name_plural = '投票'