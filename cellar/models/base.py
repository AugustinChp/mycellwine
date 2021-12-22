"""
Help on module base model:

NAME
    base model -

DESCRIPTION

CLASSES :
    models.Model
        BaseModel
            Meta
    class BaseModel(models.Model)
     |
     |  description
     |
     |  class define here:
     |
     |  class Meta
     |
     |
     |  Methods defined here:
     |
     |  save(self, data)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  find(model, instance_id)
     |      The find method is usually used to retrieve a row by ID
     |
"""

# future

# standard library
import pdb
from datetime import datetime

# third-party

# Django
from django.db import models
from django.contrib.auth.decorators import login_required
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# local Django
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    """
    A class to represent a BaseModel.

    Attributes
    ----------
    note : text
        description
    created_at : datetime
        description
    modified_at : datetime
        description
    create_by : int
        descritpion
    modified_by : int

    Methods
    -------
    save(data):
        description

    find(model, instance_id)
    """
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='%(class)s_createdby', on_delete=models.CASCADE, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User,
                                    related_name='%(class)s_modifiedby', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified_at = datetime.now()
        self.modified_by = get_current_authenticated_user()
        pdb.set_trace()
        if not self.created_by:
            self.created_by = get_current_authenticated_user()
        super().save(*args, **kwargs)

    @classmethod
    def find(cls, instance_id):

        instance = cls.objects.filter(pk=instance_id).first()
        if instance:
            return instance
        return None
