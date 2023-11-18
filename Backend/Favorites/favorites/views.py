from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FavoriteProperty

class FavoritePropertyView(APIView):
    def post(self, request):
        username = request.data.get('username')
        property_id = request.data.get('property_id')

        favorite_property, created_favorite_property = FavoriteProperty.objects.get_or_create(username=username, property_id=property_id)

        if not created_favorite_property:
            favorite_property.delete()
            return Response({'message': 'Favorite property removed successfully.'}, status=status.HTTP_200_OK)

        return Response({'message': 'Favorite property added successfully.'}, status=status.HTTP_200_OK)
