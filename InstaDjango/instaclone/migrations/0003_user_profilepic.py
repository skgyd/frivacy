# Generated by Django 2.0.2 on 2018-03-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilepic',
            field=models.CharField(default='', max_length=255),
        ),
    ]
