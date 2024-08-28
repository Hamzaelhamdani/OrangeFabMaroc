# Generated by Django 5.0.7 on 2024-08-01 22:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled News', max_length=200)),
                ('description', models.TextField(default='No description provided.')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('place', models.CharField(default='TBD', max_length=200)),
                ('tags', models.CharField(default='None', max_length=200)),
                ('banner_image', models.ImageField(default='news_banners/default_banner.jpg', upload_to='news_banners/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]