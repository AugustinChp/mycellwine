# future

# standard library

# third-party
from cloudinary.models import CloudinaryField

# Django
from django.db import models

# local Django
from .base import BaseModel


class Certification(BaseModel):
    name = models.CharField(max_length=200)
    picture = CloudinaryField('image',
                              folder='mycellwine/bottles',
                              transformation={'height': '300'},
                              format='png',
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'Certification'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
