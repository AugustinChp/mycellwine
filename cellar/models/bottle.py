# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel

from cloudinary.models import CloudinaryField


class Bottle(BaseModel):
    year = models.IntegerField(null=True, blank=True)
    picture = CloudinaryField('image',
                              folder='mycellwine/bottles',
                              transformation={'height': '300'},
                              format='png',
                              null=True,
                              blank=True)
    volume = models.ForeignKey('Volume', null=True, on_delete=models.SET_NULL)
    wine = models.ForeignKey('Wine', on_delete=models.CASCADE)
    certification = models.ManyToManyField(
        "Certification",
        through="BottleCertification",
        related_name="certification",
        blank=True,
    )

    class Meta:
        db_table = 'bottle'
        app_label = 'cellar'

    def __str__(self):
        return "{} {} - {}".format(self.wine,
                                   self.year,
                                   self.volume
                                   )