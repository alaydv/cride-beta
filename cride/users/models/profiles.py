"""Profile Model"""

# Django
from django.db import models

# Utilities
from utils.models import CRideModel


class Profile(CRideModel):
    """
    This profile holds user's data like:
            - Images
            - Biography
            - Statistics
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    image = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(
        'biography',
        max_length=500,
        blank=True
    )

    # Stats
    rides_taken = models.PositiveIntegerField(
        default=0
    )
    rides_offered = models.PositiveIntegerField(
        default=0
    )

    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered"
    )


    def __str__(self) -> str:
        """Return str of user"""
        return str(self.user)