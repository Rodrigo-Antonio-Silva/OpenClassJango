from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Singers(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        POP = 'PO'
        INDIE_POP = 'IP'
        CONTEMPORARY_COUNTRY = 'CC'
        ALTERNATIVE_RB = 'AR'
        FOLK_POP = 'FP'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default='')
    description = models.fields.CharField(max_length=2000, null=True, default='')
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], default=2000)
    active = models.fields.BooleanField(default=False)
    official_homepage = models.fields.URLField(null=True, default='')

    def __str__(self):
        return f'{self.name}'


class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        POP = 'PO'
        INDIE_POP = 'IP'
        CONTEMPORARY_COUNTRY = 'CC'
        ALTERNATIVE_RB = 'AR'
        FOLK_POP = 'FP'

    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLOT'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MIS'

    # name = models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=200, default='')
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default='')
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)], default=2000)
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=6, default='')

    singer = models.ForeignKey(Singers, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'




