from rest_framework.permissions import BasePermission


class IsUserCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.type == "customer"
    
class IsReviewOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        owner = obj.reviewer
        user = request.user

        return owner == user