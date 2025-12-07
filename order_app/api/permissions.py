from rest_framework.permissions import BasePermission


class IsOwnerFromOffer(BasePermission):
    """
    Permission class ensuring that only the business user who owns the offer
    related to the order is allowed to perform object-level actions such as
    updating or modifying the order.
    """

    def has_object_permission(self, request, view, obj):
        """
        Grant permission only if the authenticated user is the same business
        user who created the offer from which the order originated.
        """
        user = request.user
        owner = obj.business_user
        return user == owner
    

class isUserCustomer(BasePermission):
    """
    Permission class that allows an action only if the authenticated user's
    profile is of type 'customer'. Used to restrict who is allowed to place orders.
    """

    def has_permission(self, request, view):
        """
        Grant permission only when the user's profile type is 'customer'.
        """
        user = request.user
        return user.profile.type == "customer"
