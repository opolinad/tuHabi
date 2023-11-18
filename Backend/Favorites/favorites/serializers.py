from rest_framework import serializers
from .models import FavoriteProperty

class FavoritePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteProperty
        fields = '__all__'
