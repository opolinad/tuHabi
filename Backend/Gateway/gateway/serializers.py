from rest_framework import serializers

class FavoriteSerializer(serializers.Serializer):
    username = serializers.CharField()
    property_id = serializers.IntegerField()
