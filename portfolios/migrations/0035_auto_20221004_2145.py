# Generated by Django 3.2 on 2022-10-04 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0034_auto_20221004_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliodividend',
            name='dividend',
        ),
        migrations.RemoveField(
            model_name='portfoliodividend',
            name='portfolio_asset',
        ),
    ]