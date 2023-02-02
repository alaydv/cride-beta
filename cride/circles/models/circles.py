"""Circles Model"""

# Django
from django.db import models

# Utilities
from utils.models import CRideModel


class Circle(CRideModel):
    """
    Circle Model

    * A circle is a private group where rides are offered and taken by their members.
    * To join a circle a user must recive a unique invitation code from an existing circle member.
    """

    name = models.CharField(
        'circle name',
        max_length=140
    )

    slug_name = models.SlugField(
        'slug name',
        unique=True,
        max_length=40
    )

    about = models.CharField(
        'circle description',
        max_length=255
    )

    picture = models.ImageField(
        upload_to='circles/pictures/',
        blank=True,
        null=True
    )

    # Stats
    rides_taken = models.PositiveIntegerField(
        default=0
    )
    rides_offered = models.PositiveIntegerField(
        default=0
    )

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles also know as official comunities.'
    )

    is_public = models.BooleanField(
        'public circle',
        default=False,
        help_text='Public circles are listed in the main page, eveyone knows their existence.'
    )

    is_limit = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members.'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If a circle is limited, this will be limit on the number of members.'
    )


    def __str__(self) -> str:
        """Return circle name"""
        return self.name


    class Meta(CRideModel.Meta):
        """Meta class"""

        ordering = ['-rides_taken', '-rides_offered']