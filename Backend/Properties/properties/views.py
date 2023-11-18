from .models import Property
from rest_framework import generics
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend

class PropertyList(generics.ListAPIView):
    status_to_list = [3, 4, 5]
    queryset = Property.objects.filter(actual_status__in=status_to_list, price__gt=0)
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'year', 'actual_status']