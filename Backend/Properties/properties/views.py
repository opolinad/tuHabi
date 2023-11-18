from .models import Property
from rest_framework import generics
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class PropertyListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class PropertyList(generics.ListAPIView):
    status_to_list = [3, 4, 5]
    queryset = Property.objects.filter(actual_status__in=status_to_list, price__gt=0)
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'year', 'actual_status']
    pagination_class = PropertyListPagination