# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class Purchase(TrackingModel):
    purchase_place = models.CharField(max_length=200)
    unit_price = models.DecimalField(
        null=True, max_digits=10, decimal_places=2, blank=True)

    class Meta:
        db_table = 'Purchase'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
