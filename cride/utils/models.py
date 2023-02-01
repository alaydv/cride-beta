"""Abstrac models in cride utilities"""

# Django
from django.db import models


class CRideModel(models.Model):
    """
    Share Ride base model.

    CRideModel acts as an abstract class from which every other models in the project
    will inherit. This class provides every table with the following attributes:
        * created (DateTime): Store the datetime the object was create.
        * modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='DateTime on the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='DateTime on the object was last modified'
    )

    class Meta:
        """Meta options"""

        abstract=True
        get_latest_by='created'
        ordering=['-created', '-modified']