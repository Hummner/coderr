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
from rest_framework.permissions import IsAuthenticated, AllowAny


class OfferViewSet(ModelViewSet):
    """
    ViewSet for managing offers, including listing, retrieving, creating,
    updating, and deleting. It provides filtering, searching, ordering,
    pagination, permission handling, and annotated fields for min price and
    min delivery time. Authentication is required for all actions.
    """

    queryset = Offer.objects.annotate(
        min_price=Min('offer_detail__price'),
        min_delivery_time=Min('offer_detail__delivery_time_in_days')
    )

    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = OfferFilters
    ordering_fields = ['min_price', 'updated_at']
    search_fields = ['title', 'description']
    pagination_class = OfferPageNumberPagination

    def get_serializer_class(self):
        """
        Return the serializer class based on the current action.
        Listing uses a compact serializer, retrieve uses a detailed one,
        and all other actions fall back to the default serializer.
        """
        if self.action == 'list':
            return OfferListSerializer
        
        if self.action == 'retrieve':
            return OfferRetrieveSerialzier
        
        return OfferSerializer

    def get_permissions(self):
        """
        Apply different permissions depending on the performed action.
        Only business profiles may create offers, only offer owners may delete,
        and all other actions require simple authentication.
        """
        if self.action == 'create':
            return [IsAuthenticated(), isProfileTypeBusiness()]
        
        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsAuthenticated(), isUserOfferCreator()]
        
        if self.action == 'retrieve':
            return [IsAuthenticated()]

        return [AllowAny()]
    

class OfferDetailsView(RetrieveAPIView):
    """
    RetrieveAPIView for fetching detailed information about a single offer detail.
    Ensures only authenticated users can access the endpoint.
    """

    queryset = OfferDetails.objects.all()
    serializer_class = OfferDeatilsRetrieveSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Retrieve and return a single OfferDetails instance,
        using the default RetrieveAPIView implementation.
        """
        return super().get(request, *args, **kwargs)
