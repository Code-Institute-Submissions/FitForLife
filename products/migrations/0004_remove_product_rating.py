# Generated by Django 3.1.1 on 2020-12-09 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201008_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
