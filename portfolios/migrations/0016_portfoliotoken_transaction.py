# Generated by Django 3.2 on 2022-02-14 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0015_auto_20220214_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliotoken',
            name='transaction',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, to='portfolios.transaction'),
        ),
    ]