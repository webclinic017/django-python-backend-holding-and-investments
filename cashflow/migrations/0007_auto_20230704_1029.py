# Generated by Django 3.2 on 2023-07-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0006_auto_20230704_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetaverageprice',
            name='cost_brl',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='assetaverageprice',
            name='cost_usd',
            field=models.FloatField(null=True),
        ),
    ]
