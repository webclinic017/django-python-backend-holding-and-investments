# Generated by Django 3.2 on 2024-07-04 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0036_portfoliototalhistory_event_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dividendpayevent',
            options={'verbose_name': 'Distribuição de Dividendos', 'verbose_name_plural': ' Distribuição de Dividendos'},
        ),
    ]
