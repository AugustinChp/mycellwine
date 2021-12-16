# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel


class Volume(BaseModel):
    name = models.CharField(max_length=200)
    volume = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'Volume'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name} ({self.volume})'
