# Generated by Django 5.0.1 on 2024-01-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_band_year_formed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='year_formed',
            new_name='year',
        ),
    ]