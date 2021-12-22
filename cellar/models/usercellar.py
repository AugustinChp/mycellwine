# third-party

# Django
from django.db import models

# local Django
from .base import BaseModel
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserCellar(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cellar = models.ForeignKey('Cellar', on_delete=models.CASCADE)

    class Meta:
        db_table = 'UserCellar'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.user} - {self.cellar}'
