# Generated by Django 3.1.1 on 2020-12-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='has_discount',
            field=models.BooleanField(default=False),
        ),
    ]
