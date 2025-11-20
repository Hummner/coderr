from rest_framework import generics
from .serializers import BusinessListSerializer
from profile_app.models import Profile




class BusinessProfileListView(generics.ListAPIView):
    serializer_class = BusinessListSerializer
    queryset = Profile.objects.all()


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)