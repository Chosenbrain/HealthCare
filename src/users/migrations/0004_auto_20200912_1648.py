# Generated by Django 3.1 on 2020-09-12 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='patient',
        ),
        migrations.AddField(
            model_name='chat',
            name='room_name',
            field=models.CharField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
    ]
