# Generated by Django 3.2 on 2023-07-13 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0046_assethistoricalprice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssetHistoricalPrice',
        ),
    ]
