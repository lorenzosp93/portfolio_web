# Generated by Django 2.2 on 2019-05-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20190506_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='current',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experience',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
