from rest_framework.viewsets import ModelViewSet
from ..models import Offer
from .serializers import OfferSerializer, OfferListSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isProfileTypeBusiness
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OfferFilters
from rest_framework import filters, pagination
from django.db.models import Min
from .pagination import OfferPageNumberPagination
from rest_framework.pagination import Response


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.annotate(
        min_price = Min('offer_detail__price'),
        min_delivery_time = Min('offer_detail__delivery_time_in_days')
    )
    authentication_classes = [TokenAuthentication]
    permission_classes = [isProfileTypeBusiness]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = OfferFilters
    ordering_fields = ['min_price', 'updated_at']
    search_fields = [ 'title', 'description']
    pagination_class = OfferPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return OfferListSerializer
        return OfferSerializer

    def list(self, request, *args, **kwargs):


        


        return super().list(request, *args, **kwargs)
