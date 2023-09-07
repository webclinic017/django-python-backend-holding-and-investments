# Generated by Django 3.2 on 2023-07-19 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0026_alter_currencytransaction_transaction_type'),
        ('equity', '0018_redemptionevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetValuationEvent',
            fields=[
                ('quotahistory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equity.quotahistory')),
            ],
            bases=('equity.quotahistory',),
        ),
        migrations.CreateModel(
            name='DividendPayEvent',
            fields=[
                ('currencytransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cashflow.currencytransaction')),
            ],
            bases=('cashflow.currencytransaction',),
        ),
        migrations.CreateModel(
            name='DividendReceiveEvent',
            fields=[
                ('currencytransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cashflow.currencytransaction')),
            ],
            bases=('cashflow.currencytransaction',),
        ),
        migrations.AlterField(
            model_name='quotahistory',
            name='event_type',
            field=models.CharField(choices=[('deposit', 'deposit'), ('withdraw', 'withdraw'), ('valuation', 'valuation'), ('dividend receive', 'dividend receive'), ('dividend payment', 'dividend payment')], default='deposit', max_length=20),
        ),
    ]