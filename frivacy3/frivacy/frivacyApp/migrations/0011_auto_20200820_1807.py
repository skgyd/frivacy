# Generated by Django 3.1 on 2020-08-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frivacyApp', '0010_auto_20200820_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]