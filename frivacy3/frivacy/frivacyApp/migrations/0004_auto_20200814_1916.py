# Generated by Django 3.1 on 2020-08-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frivacyApp', '0003_auto_20200814_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
