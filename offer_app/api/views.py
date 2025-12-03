from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from ..models import Offer, OfferDetails
from .serializers import OfferSerializer, OfferListSerializer, OfferRetrieveSerialzier, OfferDeatilsRetrieveSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isProfileTypeBusiness, isUserOfferCreator
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OfferFilters
from rest_framework import filters, pagination
from django.db.models import Min
from .pagination import OfferPageNumberPagination
from rest_framework.pagination import Response
from rest_framework.permissions import IsAuthenticated


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.annotate(
        min_price = Min('offer_detail__price'),
        min_delivery_time = Min('offer_detail__delivery_time_in_days')
    )
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = OfferFilters
    ordering_fields = ['min_price', 'updated_at']
    search_fields = [ 'title', 'description']
    pagination_class = OfferPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return OfferListSerializer
        
        if self.action == 'retrieve':
            return OfferRetrieveSerialzier
        
        return OfferSerializer

    def get_permissions(self):

        if self.action == 'create':
            return [isProfileTypeBusiness()]
        if self.action == 'destroy':
            return [isUserOfferCreator()]

        return [IsAuthenticated()]
    

class OfferDetailsView(RetrieveAPIView):
    queryset = OfferDetails.objects.all()
    serializer_class = OfferDeatilsRetrieveSerializer
    authentication_classes = [TokenAuthentication]
