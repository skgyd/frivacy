# Generated by Django 3.1 on 2020-08-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frivacyApp', '0005_follower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.CharField(max_length=20)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(default='', max_length=20)),
                ('comment', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
