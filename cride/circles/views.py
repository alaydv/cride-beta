"""Views to list circles"""

# Django
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Model
from .models.circles import Circle


# Views
@api_view(['GET'])
def list_circles(request):
    """List circles"""

    circles = Circle.objects.all()
    public = circles.filter(is_public=True)

    data = []
    for circle in circles:
        data.append( {
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit,
        })

    return Response(data)