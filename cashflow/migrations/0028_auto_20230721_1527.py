# Generated by Django 3.2 on 2023-07-21 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0027_auto_20230720_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencytransfer',
            options={'ordering': ['-transfer_date'], 'verbose_name_plural': ' Transferências mesma moeda'},
        ),
        migrations.AlterModelOptions(
            name='internationalcurrencytransfer',
            options={'ordering': ['-transfer_date'], 'verbose_name_plural': 'Transferências Internacionais'},
        ),
    ]