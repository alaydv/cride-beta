"""Circle Admin"""

# Django
from django.contrib import admin

# Models
from cride.circles.models import Circle


@admin.register(Circle)
class CirclesAdminConfig(admin.ModelAdmin):
    """Register of the model"""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limit',
        'members_limit'
    )

    search_fiels = ('slug_name', 'name')

    list_filter = (
        'is_limit',
        'verified',
        'is_public'
    )