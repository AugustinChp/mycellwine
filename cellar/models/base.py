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
from datetime import datetime

# third-party

# Django
from django.db import models

# local Django


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
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, data, *args, **kwargs):
        '''
        description

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:

        '''
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        super().save(*args, **kwargs)

    @classmethod
    def find(cls, instance_id):

        instance = cls.objects.filter(pk=instance_id).first()
        if instance:
            return instance
        return None
