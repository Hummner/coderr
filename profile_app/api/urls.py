from django.urls import path
from .views import BusinessProfileListView, CustomerProfileListView, ProfileView
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r"", ProfileView, basename='profile')


urlpatterns = [
    path('business/', BusinessProfileListView.as_view(), name='business_profiles'),
    path('customer/', CustomerProfileListView.as_view(), name='customer_profiles'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)