# future

# standard library

# third-party

# Django
from django.db import models
from django.utils import timezone

# local Django
from helpers.models import TrackingModel


class BottleOutlet(TrackingModel):
    date = models.DateTimeField(null=False, default=timezone.now)
    event = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'BottleOutlet'
        app_label = 'cellar'
