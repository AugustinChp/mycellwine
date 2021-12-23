# future

# standard library
import uuid
# third-party

# Django
from django.db import models

# local Django
from django_currentuser.middleware import get_current_user


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'account.User', default=get_current_user, on_delete=models.CASCADE, blank=True, related_name='%(class)s_createdby')
    modified_by = models.ForeignKey(
        'account.User', default=get_current_user, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_modifiedby')

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        self.modified_by = get_current_user()
        if not self.created_by:
            self.created_by = get_current_user()
        super().save(*args, **kwargs)
