# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel


class TechnicalSheetFood(BaseModel):
    technical_sheet = models.ForeignKey(
        'TechnicalSheet', on_delete=models.CASCADE)
    food = models.ForeignKey('Food', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TechnicalSheetFood'
        app_label = 'cellar'

    def __str__(self):
        return f'Technical sheet n°{self.technical_sheet.id} - {self.food.name}'
