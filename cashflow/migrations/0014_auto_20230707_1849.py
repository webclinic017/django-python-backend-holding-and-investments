# Generated by Django 3.2 on 2023-07-07 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0013_rename_assetaveragehistory_transactionshistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactionshistory',
            options={'ordering': ['-transaction_date'], 'verbose_name': 'Histórico de Transações', 'verbose_name_plural': 'Históricos de Transações'},
        ),
        migrations.RenameField(
            model_name='transactionshistory',
            old_name='timestamp',
            new_name='transaction_date',
        ),
    ]