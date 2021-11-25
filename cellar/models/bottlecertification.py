# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel


class BottleCertification(BaseModel):
    bottle = models.ForeignKey('Bottle', on_delete=models.CASCADE)
    certification = models.ForeignKey(
        'Certification', on_delete=models.CASCADE)

    class Meta:
        db_table = 'BottleCertification'
        app_label = 'cellar'
