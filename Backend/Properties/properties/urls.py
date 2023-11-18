from django.urls import path
from .views import PropertyList, VerifyProperty

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('property/<int:property_id>', VerifyProperty.as_view(), name='property-detail'),
]
