from rest_framework.routers import DefaultRouter
from .views import OrderViewset

router = DefaultRouter()
router.register(r"", OrderViewset, basename='orders')

urlpatterns = router.urls