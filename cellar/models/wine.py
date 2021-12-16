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
from .base import BaseModel


class Wine(BaseModel):
    cuvee = models.CharField(max_length=200, blank=True, default="")
    terroir = models.CharField(max_length=200, blank=True, default="")
    wine_type = models.ForeignKey(
        "WineType", null=True, on_delete=models.SET_NULL)
    classification = models.ForeignKey(
        "Classification", null=True, on_delete=models.SET_NULL, blank=True
    )
    appellation = models.ForeignKey(
        "Appellation", null=True, on_delete=models.SET_NULL)
    domain = models.ForeignKey('Domain', null=True, on_delete=models.SET_NULL)
    grape_varieties = models.ManyToManyField(
        "GrapeVariety",
        through="WineGrapeVariety",
        related_name="grape_varieties",
        blank=True,
    )

    class Meta:
        db_table = 'Wine'
        app_label = 'cellar'

    def __str__(self):
        return f'{self.domain.name} {self.cuvee} {self.appellation}'
