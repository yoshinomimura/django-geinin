# Generated by Django 3.2.7 on 2021-12-12 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comedians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_funny', models.BooleanField(default=True, verbose_name='面白い')),
                ('user_agent', models.CharField(blank=True, max_length=128, verbose_name='User Agent')),
                ('ip_address', models.CharField(blank=True, max_length=128, verbose_name='IP Address')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日')),
                ('comedian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='comedians.comedian', verbose_name='芸人')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polls', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': '投票',
                'verbose_name_plural': '投票',
            },
        ),
    ]
