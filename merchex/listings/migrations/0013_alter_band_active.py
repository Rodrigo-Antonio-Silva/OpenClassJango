# Generated by Django 5.0.1 on 2024-01-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_alter_band_biography_alter_band_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
