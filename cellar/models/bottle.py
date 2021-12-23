# future

# standard library

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel

from cloudinary.models import CloudinaryField


class Bottle(TrackingModel):
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
    technical_sheet = models.ForeignKey(
        'TechnicalSheet', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Bottle'
        app_label = 'cellar'

    def __str__(self):
        return "{} {} - {}".format(self.wine,
                                   self.year,
                                   self.volume
                                   )
