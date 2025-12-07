from rest_framework.viewsets import ModelViewSet
from review_app.models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserCustomer, IsReviewOwner
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReviewFilters


class ReviewViewset(ModelViewSet):
    """
    ViewSet responsible for listing, creating, updating, and deleting reviews.
    Applies filtering, ordering, authentication, and permission rules to ensure
    that only customers can submit reviews and only the review owner may edit
    or delete them.
    """

    queryset = Review.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ReviewFilters
    ordering_fields = ['rating', '-updated_at']

    def get_permissions(self):
        """
        Dynamically assign permissions based on the action being performed.
        Only customers may create reviews, only the review owner may update or
        delete a review, and all other actions simply require authentication.
        """
        if self.action == 'create':
            return [IsUserCustomer()]

        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsReviewOwner()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        """
        Automatically set the authenticated user as the reviewer when a new
        review is created, ensuring ownership and traceability.
        """
        serializer.save(reviewer=self.request.user)
