# Generated by Django 3.0.6 on 2020-06-17 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_blog_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='View_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Blog')),
            ],
        ),
    ]
