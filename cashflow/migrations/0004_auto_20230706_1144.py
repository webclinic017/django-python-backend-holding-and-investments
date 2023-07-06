# Generated by Django 3.2 on 2023-07-06 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brokers', '0007_broker_main_currency'),
        ('cashflow', '0003_expense_income'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assettransaction',
            options={'ordering': ['-transaction_date'], 'verbose_name': 'Compra e Venda de Ativo', 'verbose_name_plural': 'Compra e Venda de Ativos'},
        ),
        migrations.AlterField(
            model_name='internationalcurrencytransfer',
            name='from_broker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='international_transfer_from', to='brokers.broker'),
        ),
        migrations.AlterField(
            model_name='internationalcurrencytransfer',
            name='from_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_international_transfers', to='cashflow.currencytransaction'),
        ),
        migrations.AlterField(
            model_name='internationalcurrencytransfer',
            name='to_broker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='intternational_transfer_to', to='brokers.broker'),
        ),
        migrations.AlterField(
            model_name='internationalcurrencytransfer',
            name='to_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_international_transfers', to='cashflow.currencytransaction'),
        ),
    ]
