# future

# standard library


# third-party

# Django
from django.db import models
from django.utils import timezone

# local Django
from .base import BaseModel


class AddBottle(BaseModel):
    date = models.DateTimeField(null=False, default=timezone.now)
    event = models.TextField(null=True, blank=True)
    person = models.ForeignKey(
        'Person', null=True, blank=True, on_delete=models.SET_NULL)
    purchase = models.ForeignKey(
        'Purchase', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'AddBottle'
        app_label = 'cellar'
