from rest_framework.viewsets import ModelViewSet
from ..models import Offer
from .serializers import OfferSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isProfileTypeBusiness
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OfferFilters
from rest_framework import filters
from django.db.models import Min


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.annotate(
        min_price = Min('offer_detail__price')
    )
    serializer_class = OfferSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [isProfileTypeBusiness]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OfferFilters
    ordering_fields = ['min_price']
    
