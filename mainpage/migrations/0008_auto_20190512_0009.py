# Generated by Django 2.2 on 2019-05-11 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.IntegerField(choices=[(1, 'basic'), (2, 'advanced'), (3, 'expert'), (4, 'professional')]),
        ),
    ]
