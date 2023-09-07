# Generated by Django 3.2 on 2023-07-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0023_remove_investevent_trade_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investevent',
            name='trade_type',
        ),
        migrations.AddField(
            model_name='investevent',
            name='asset_price_brl',
            field=models.FloatField(default=0),
        ),
    ]