# Generated by Django 3.0.6 on 2020-06-23 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_pricing_pricingservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category',
        ),
    ]
