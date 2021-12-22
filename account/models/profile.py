# future

# standard library
from datetime import datetime

# third-party

# Django
from django.db import models

# local Django
from cellar.models import Country
from django.conf import settings
from django_currentuser.middleware import get_current_authenticated_user

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User,
                                    related_name='%(class)s_modifiedby', null=True, blank=True, on_delete=models.SET_NULL)

    country = models.ForeignKey(
        Country, null=True, on_delete=models.SET_NULL)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.modified_at = datetime.now()
        self.modified_by = get_current_authenticated_user()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name
