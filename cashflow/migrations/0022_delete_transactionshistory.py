# Generated by Django 3.2 on 2023-07-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0015_alter_portfoliodividend_transaction_history'),
        ('cashflow', '0021_auto_20230713_1809'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransactionsHistory',
        ),
    ]
