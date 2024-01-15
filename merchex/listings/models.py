from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        ROCK = 'RO'

    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLOT'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MIS'

    name = models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=200, default='')
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default='')
    biography = models.fields.CharField(max_length=1000, default='')
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], default=2000)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length=200, default='')
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(default=2000)
    type = models.fields.CharField(choices=Type.choices, max_length=6, default='')


