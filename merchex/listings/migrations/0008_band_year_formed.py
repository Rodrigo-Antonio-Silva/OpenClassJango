# Generated by Django 5.0.1 on 2024-01-15 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
            preserve_default=False,
        ),
    ]