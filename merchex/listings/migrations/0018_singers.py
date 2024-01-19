# Generated by Django 5.0.1 on 2024-01-18 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0017_alter_band_official_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Singers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "band",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="listings.band",
                    ),
                ),
            ],
        ),
    ]
