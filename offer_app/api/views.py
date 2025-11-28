from rest_framework.viewsets import ModelViewSet
from ..models import Offer
from .serializers import OfferSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isProfileTypeBusiness


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [isProfileTypeBusiness]
    
