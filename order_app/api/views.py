from rest_framework.viewsets import ModelViewSet
from ..models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerFromOffer, isUserCustomer


class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(Q(customer_user=user) | Q(business_user=user))
        return queryset
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsOwnerFromOffer()]
        if self.action == 'destroy':
            return [IsAdminUser()]
        
        if self.action == 'create':
            return [isUserCustomer()]

        return [IsAuthenticated()]