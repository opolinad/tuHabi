from rest_framework import status
from rest_framework.views import APIView
from .serializers import FavoriteSerializer
from rest_framework.response import Response
from .utils import is_property_valid, favorite_property, list_properties

class FavoriteView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = FavoriteSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            username = serializer.validated_data['username']
            property_id = serializer.validated_data['property_id']

            valid_property = is_property_valid(property_id)

            if valid_property:
                favorite_property_response = favorite_property(username, property_id)
                return Response({'message': favorite_property_response['message']}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid property_id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('*************************************************')
            print('Error', str(e))
            print('*************************************************')
            return Response({'message': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PropertiesView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            query_params = request.GET
            properties_list = list_properties(query_params)
            return Response(properties_list, status=status.HTTP_200_OK)
        except Exception as e:
            print('*************************************************')
            print('Error', str(e))
            print('*************************************************')
            return Response({'message': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
