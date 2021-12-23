# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class TechnicalSheet(TrackingModel):
    alcohol_level = models.DecimalField(max_digits=4, decimal_places=2)
    started_apogee = models.IntegerField(null=True, blank=True)
    stopped_apogee = models.IntegerField(null=True, blank=True)
    mark = models.IntegerField(default=0, blank=True)
    tasting_temperature = models.IntegerField(default=0, blank=True)
    storage_temperature = models.IntegerField(default=0, blank=True)
    food_paring = models.ManyToManyField(
        "Food",
        through="TechnicalSheetFood",
        related_name="food_paring",
        blank=True,
    )

    class Meta:
        db_table = 'TechnicalSheet'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
