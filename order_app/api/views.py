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
    """
    ViewSet responsible for creating, retrieving, updating, and deleting orders.
    It restricts access based on who owns the offer, user role, and authentication
    status while returning only the orders related to the requesting user.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        Return only the orders where the authenticated user is either the customer
        or the business user, ensuring users can access only their relevant orders.
        """
        user = self.request.user
        queryset = Order.objects.filter(Q(customer_user=user) | Q(business_user=user))
        return queryset
    
    def get_permissions(self):
        """
        Determine permissions dynamically based on the action:
        - Only the offer owner may update orders
        - Only admins may delete orders
        - Only customers may create orders
        - All other actions require authentication
        """
        if self.action in ['update', 'partial_update']:
            return [IsOwnerFromOffer()]
        if self.action == 'destroy':
            return [IsAdminUser()]
        if self.action == 'create':
            return [isUserCustomer()]
        return [IsAuthenticated()]
    

class OrderInProgress(APIView):
    """
    API endpoint that returns how many orders are currently in progress
    for a given business user. Only authenticated users may access this.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve the count of in-progress orders for the given user ID.
        Returns an error if the user does not exist.
        """
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        count = Order.objects.filter(
            Q(business_user_id=pk) & Q(status='in_progress')
        ).count()

        return Response({'order_count': count})
    

class OrderCompleted(APIView):
    """
    API endpoint that returns how many orders were completed
    for a given business user. Only authenticated users may access this.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve the count of completed orders for the given user ID.
        Returns an error response if the user does not exist.
        """
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        count = Order.objects.filter(
            Q(business_user_id=pk) & Q(status='completed')
        ).count()

        return Response({'completed_order_count': count})
