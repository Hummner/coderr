from django.urls import path
from .views import BusinessProfileListView, CustomerProfileListView, ProfileView
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r"", ProfileView, basename='profile')


urlpatterns = [

]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)