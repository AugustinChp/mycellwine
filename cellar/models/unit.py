# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class Unit(TrackingModel):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=5)
    convertion = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        db_table = 'Unit'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
