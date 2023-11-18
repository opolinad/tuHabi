from django.urls import path
from .views import FavoriteView, PropertiesView

urlpatterns = [
    path('favorite-property/', FavoriteView.as_view(), name='favorite'),
    path('properties/', PropertiesView.as_view(), name='properties'),
]
