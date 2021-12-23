# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class GrapeVariety(TrackingModel):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    class Meta:
        db_table = 'GrapeVariety'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
