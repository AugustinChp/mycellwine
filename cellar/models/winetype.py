# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class WineType(TrackingModel):
    name = models.CharField(max_length=200)
    fra_name = models.CharField(max_length=200, default='')

    class Meta:
        db_table = 'WineType'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
