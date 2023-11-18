from django.urls import path
from .views import FavoritePropertyView

urlpatterns = [
    path('favorite-property/', FavoritePropertyView.as_view(), name='favorite-property'),
]
