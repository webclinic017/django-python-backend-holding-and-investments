# Generated by Django 3.2 on 2022-05-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0025_remove_transaction_broker_average_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='profit',
            field=models.FloatField(default=0, editable=False),
        ),
    ]