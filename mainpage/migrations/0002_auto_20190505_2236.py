# Generated by Django 2.2 on 2019-05-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='experience',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
