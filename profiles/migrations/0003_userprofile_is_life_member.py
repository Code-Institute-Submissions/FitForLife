# Generated by Django 3.1.1 on 2020-11-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_is_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_life_member',
            field=models.BooleanField(default=False),
        ),
    ]
