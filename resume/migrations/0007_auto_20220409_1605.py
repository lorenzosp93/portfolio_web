# Generated by Django 3.2 on 2022-04-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_project_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['-level']},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(0, 'Idea'), (1, 'Started'), (2, 'Ongoing'), (3, 'Completed')], default=3),
        ),
    ]
