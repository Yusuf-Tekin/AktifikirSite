# Generated by Django 3.1.4 on 2021-01-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210104_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='AppPhoto',
            field=models.ImageField(upload_to='images'),
        ),
    ]
