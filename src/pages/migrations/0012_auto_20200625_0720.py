# Generated by Django 3.0.6 on 2020-06-25 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20200623_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricing',
            old_name='services',
            new_name='service',
        ),
    ]
