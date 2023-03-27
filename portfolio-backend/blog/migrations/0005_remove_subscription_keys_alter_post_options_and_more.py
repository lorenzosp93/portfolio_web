# Generated by Django 4.1.7 on 2023-02-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_keys_subscription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='keys',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='submit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='thumb/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.DeleteModel(
            name='Keys',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]