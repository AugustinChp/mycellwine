# future

# standard library
from datetime import datetime

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel
from cellar.models import Country
from django.conf import settings


class Profile(TrackingModel):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        if self.first_name is None or self.last_name is None:
            return self.user.username
        return self.get_full_name
