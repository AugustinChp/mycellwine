# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class Appellation(TrackingModel):
    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    appellation_type = models.ForeignKey(
        'AppellationType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Appellation'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
