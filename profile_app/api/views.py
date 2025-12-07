from rest_framework import generics, viewsets, mixins
from .serializers import BusinessListSerializer, CustomerListSerializer, ProfileSerializer
from profile_app.models import Profile
from rest_framework.authentication import TokenAuthentication
from .permissions import ProfilePatchPermission
from rest_framework.permissions import IsAuthenticated


class BusinessProfileListView(generics.ListAPIView):
    """
    API endpoint for listing all business profiles. This view returns only users
    whose profile type is 'business' and requires authentication for access.
    """

    serializer_class = BusinessListSerializer
    queryset = Profile.objects.filter(type="business")
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CustomerProfileListView(generics.ListAPIView):
    """
    API endpoint for listing all customer profiles. Only profiles with the type
    'customer' are included, and the requesting user must be authenticated.
    """

    serializer_class = CustomerListSerializer
    queryset = Profile.objects.filter(type="customer")
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProfileView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """
    ViewSet handling retrieval and update of individual user profiles. Update
    operations use a custom permission class to ensure only the correct user
    may modify their own profile, while retrieval only requires authentication.
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        """
        Dynamically assign permissions based on the action. Updates require a
        stricter permission (ProfilePatchPermission), while retrieval simply
        requires the user to be authenticated.
        """
        if self.action in ['update', 'partial_update']:
            return [ProfilePatchPermission()]

        return [IsAuthenticated()]
