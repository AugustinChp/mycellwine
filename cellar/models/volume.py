# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel

DEFAULT_UNIT_ID = 2


class Volume(TrackingModel):
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.ForeignKey(
        'Unit', on_delete=models.CASCADE, default=DEFAULT_UNIT_ID)

    class Meta:
        db_table = 'Volume'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name} ({self.volume})'
