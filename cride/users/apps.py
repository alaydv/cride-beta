"""User apps"""

# Django
from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    name: str = 'cride.users'
    verbose_name: str = 'Users'