# Generated by Django 3.2 on 2023-07-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0020_alter_transactionshistory_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assettransactioncalculation',
            name='last_transaction',
        ),
        migrations.RemoveField(
            model_name='assettransactioncalculation',
            name='portfolio_investment',
        ),
        migrations.RemoveField(
            model_name='transactionshistory',
            name='portfolio_investment',
        ),
        migrations.RemoveField(
            model_name='transactionshistory',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='AssetTransaction',
        ),
        migrations.DeleteModel(
            name='AssetTransactionCalculation',
        ),
    ]
