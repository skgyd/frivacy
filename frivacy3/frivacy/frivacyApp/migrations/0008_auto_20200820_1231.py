# Generated by Django 3.1 on 2020-08-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frivacyApp', '0007_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.CharField(max_length=20)),
                ('liker', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
