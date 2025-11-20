from django.urls import path
from .views import BusinessProfileListView


urlpatterns = [
    path('business/', BusinessProfileListView.as_view(), name='business_profiles'),
]