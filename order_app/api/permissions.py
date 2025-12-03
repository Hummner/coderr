from rest_framework.permissions import BasePermission

class IsOwnerFromOffer(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        owner = obj.business_user

        return user == owner
    
class isUserCustomer(BasePermission):


    def has_permission(self, request, view):
        user = request.user

        return user.profile.type == "customer"