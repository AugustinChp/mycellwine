# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class Classification(TrackingModel):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'Clasification'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
