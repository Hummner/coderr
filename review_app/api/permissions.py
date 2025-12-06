from rest_framework.permissions import BasePermission


class IsUserCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.type == "customer"