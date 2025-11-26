from rest_framework import generics, viewsets, mixins
from .serializers import BusinessListSerializer, CustomerListSerializer, ProfileSerializer
from profile_app.models import Profile




class BusinessProfileListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    queryset = Profile.objects.filter(type="business")

class CustomerProfileListView(generics.ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Profile.objects.filter(type="customer")

class ProfileView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    