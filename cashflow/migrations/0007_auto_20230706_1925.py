# Generated by Django 3.2 on 2023-07-06 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0006_assetaverageprice_asset_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetaverageprice',
            name='asset_transaction',
        ),
        migrations.AddField(
            model_name='assetaverageprice',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
