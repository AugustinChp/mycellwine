# future

# standard library

# third-party
from cloudinary.models import CloudinaryField

# Django
from django.db import models

# local Django
from .base import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=200)
    picture = CloudinaryField('image',
                              folder='mycellwine/countries',
                              format='png',
                              null=True,
                              blank=True)

    class Meta:
        db_table = 'Country'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.name}'
