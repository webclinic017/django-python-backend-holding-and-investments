# Generated by Django 3.2 on 2023-07-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0004_auto_20230706_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetaverageprice',
            name='total_brl',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='assetaverageprice',
            name='total_shares',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='assetaverageprice',
            name='total_usd',
            field=models.FloatField(default=0),
        ),
    ]