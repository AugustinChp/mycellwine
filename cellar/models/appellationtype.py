# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class AppellationType(TrackingModel):
    name = models.CharField(max_length=200)
    origin = models.ForeignKey('Country', on_delete=models.CASCADE)

    class Meta:
        db_table = 'AppellationType'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
