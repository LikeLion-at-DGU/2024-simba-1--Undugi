# Generated by Django 5.0.3 on 2024-06-25 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('ranking_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_calories_burned', models.FloatField(default=0)),
                ('rank', models.PositiveIntegerField(blank=True, null=True)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ranking', to='accounts.profile')),
            ],
        ),
    ]
