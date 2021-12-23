# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class CellarBottleAdd(TrackingModel):
    cellar_bottle = models.ForeignKey('CellarBottle', on_delete=models.CASCADE)
    add_bottle = models.ForeignKey('AddBottle', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'CellarBottleAdd'
        app_label = 'cellar'
