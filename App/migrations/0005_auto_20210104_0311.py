# Generated by Django 3.1.4 on 2021-01-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210104_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='AppPhoto',
            field=models.ImageField(default='DefaultAppImage.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='idea',
            name='IdeaPhoto',
            field=models.ImageField(default='DefaultIdeaImage.png', upload_to=''),
        ),
    ]
