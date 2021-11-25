# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel


class Food(BaseModel):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'Food'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
