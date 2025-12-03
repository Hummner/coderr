from rest_framework.permissions import BasePermission

class IsOwnerFromOffer(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        owner = obj.business_user

        return user == owner