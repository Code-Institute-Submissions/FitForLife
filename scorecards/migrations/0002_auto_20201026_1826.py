# Generated by Django 3.1.1 on 2020-10-26 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('scorecards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorecard',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='scorecard',
            name='user_profile_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scorecards', to='profiles.userprofile'),
        ),
    ]
