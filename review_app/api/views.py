from rest_framework.viewsets import ModelViewSet
from review_app.models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]