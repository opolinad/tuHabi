from .models import Property
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import PropertySerializer
from rest_framework.response import Response
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

class VerifyProperty(APIView):
    def get(self, request, property_id):
        try:
            property_obj = Property.objects.get(id=property_id)
            serializer = PropertySerializer(property_obj)
            return Response({'exists': True, 'message': 'Property exists'})
        except Property.DoesNotExist:
            return Response({'exists': False, 'message': 'Property does not exist'}, status=status.HTTP_404_NOT_FOUND)