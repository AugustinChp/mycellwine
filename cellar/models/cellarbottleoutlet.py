# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel


class CellarBottleOutlet(BaseModel):
    cellar_bottle = models.ForeignKey('CellarBottle', on_delete=models.CASCADE)
    bottle_outlet = models.ForeignKey('BottleOutlet', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = 'CellarBottleOutlet'
        app_label = 'cellar'
