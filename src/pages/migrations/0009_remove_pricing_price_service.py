# Generated by Django 3.0.6 on 2020-06-23 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_pricing_price_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='price_service',
        ),
    ]
