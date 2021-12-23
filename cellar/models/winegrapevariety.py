"""
Help on module base model:

NAME
    base model - Automatically formats Python code to conform to the PEP 8 style guide.

DESCRIPTION
    Fixes that only need be done once can be added by adding a function of the form
    "fix_<code>(source)" to this module. They should return the fixed source code.
    These fixes are picked up by apply_global_fixes().

    Fixes that depend on pycodestyle should be added as methods to FixPEP8. See the
    class documentation for more information.

FILE
./cellar/model/appellation.py

CLASSES :
    models.Model
        BaseModel
            Meta
    class BaseModel(models.Model)
     |  BaseModel(model)
     |
     |  The smallest unbreakable unit that can be reflowed.
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

# third-party

# Django
from django.db import models

# local Django
from helpers.models import TrackingModel


class WineGrapeVariety(TrackingModel):
    wine = models.ForeignKey('Wine', on_delete=models.CASCADE)
    grape_variety = models.ForeignKey('GrapeVariety', on_delete=models.CASCADE)
    rate = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'WineGrapeVariety'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.wine} - {self.grapevariety}'
