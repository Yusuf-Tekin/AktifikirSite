# Generated by Django 3.1.4 on 2021-01-05 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_app_applink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='IdeaPhoto',
        ),
    ]