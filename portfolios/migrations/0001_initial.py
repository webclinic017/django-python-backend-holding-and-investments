# Generated by Django 3.2 on 2021-12-21 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares_amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('share_average_price_brl', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_cost_brl', models.DecimalField(decimal_places=2, max_digits=18)),
                ('total_today_brl', models.DecimalField(decimal_places=2, max_digits=18)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investments.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
            ],
        ),
    ]
