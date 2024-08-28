# Generated by Django 5.0.7 on 2024-08-04 12:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_news_created_at_remove_news_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='banner_image',
            field=models.ImageField(default='news_banners/default_banner.jpg', upload_to='news_banners/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AlterField(
            model_name='news',
            name='place',
            field=models.CharField(default='TBD', max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='Untitled News', max_length=200),
        ),
    ]