# Generated by Django 5.0.1 on 2024-03-02 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_bot', '0006_alter_backupsenderbot_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogSenderBot',
        ),
    ]
