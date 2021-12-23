# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserCellar(TrackingModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cellar = models.ForeignKey('Cellar', on_delete=models.CASCADE)

    class Meta:
        db_table = 'UserCellar'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.user} - {self.cellar}'
