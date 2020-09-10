# Generated by Django 3.1 on 2020-08-21 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subheading', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plans', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('service', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Pricingservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=250)),
                ('pricing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.pricing')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('summary', models.TextField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
            ],
        ),
    ]
