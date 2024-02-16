# Generated by Django 3.2 on 2024-02-16 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0006_auto_20240215_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='KidsButtons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_dividends', models.BooleanField(default=True)),
                ('show_quests', models.BooleanField(default=True)),
                ('show_earnings', models.BooleanField(default=True)),
                ('show_expenses', models.BooleanField(default=True)),
                ('show_games', models.BooleanField(default=False)),
                ('show_events', models.BooleanField(default=True)),
                ('show_goals', models.BooleanField(default=False)),
                ('show_education', models.BooleanField(default=False)),
                ('show_growth', models.BooleanField(default=True)),
                ('show_banks', models.BooleanField(default=True)),
                ('show_explore', models.BooleanField(default=True)),
                ('belongs_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_buttons', to='kids.kidprofile')),
            ],
            options={
                'verbose_name_plural': 'KidsButtons',
            },
        ),
    ]
