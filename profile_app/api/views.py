from rest_framework import generics, viewsets, mixins
from .serializers import BusinessListSerializer, CustomerListSerializer, ProfileSerializer
from profile_app.models import Profile
from rest_framework.authentication import TokenAuthentication
from .permissions import ProfilePatchPermission
from rest_framework.permissions import IsAuthenticated




class BusinessProfileListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    queryset = Profile.objects.filter(type="business")
    authentication_classes = [TokenAuthentication]

class CustomerProfileListView(generics.ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Profile.objects.filter(type="customer")
    authentication_classes = [TokenAuthentication]

class ProfileView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):

        if self.action in ['update', 'partial_update']:
            return [ProfilePatchPermission()]
        return [IsAuthenticated()]