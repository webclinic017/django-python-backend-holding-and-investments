# Generated by Django 3.2 on 2021-12-22 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': '   Portfolios'},
        ),
        migrations.AlterModelOptions(
            name='portfolioasset',
            options={'verbose_name_plural': '  Portfolio Assets'},
        ),
    ]
