from rest_framework.viewsets import ModelViewSet
from ..models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerFromOffer, isUserCustomer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


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
    

class OrderInProgress(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        count = Order.objects.filter(Q(business_user_id=pk) & Q(status='in_progress') ).count()
        return Response({'order_count': count})
    
class OrderCompleted(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        count = Order.objects.filter(Q(business_user_id=pk) & Q(status='completed') ).count()
        return Response({'order_count': count})
    
 