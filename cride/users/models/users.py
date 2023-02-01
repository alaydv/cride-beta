"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
    User model

    Extends from Django's AbstractUser, change the username field to email, and add
    some extra fields.
    """

    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'This email already exists'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish user and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to True when user have verified its email'
    )


    def __str__(self) -> str:
        """Return Username"""
        return self.username

    def get_short_name(self) -> str:
        """Return Username as shor name"""
        return self.username