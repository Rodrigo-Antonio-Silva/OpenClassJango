# Generated by Django 5.0.1 on 2024-01-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_remove_band_biography_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]
