# Generated by Django 5.0.1 on 2024-03-01 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='telegrambot',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='telegrambot',
            name='app_name',
        ),
    ]
