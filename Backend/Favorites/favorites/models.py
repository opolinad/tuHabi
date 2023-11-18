from django.db import models

class FavoriteProperty(models.Model):
    username = models.CharField(unique=True, max_length=255)
    property_id = models.IntegerField()

    class Meta:
        unique_together = ('username', 'property_id')
