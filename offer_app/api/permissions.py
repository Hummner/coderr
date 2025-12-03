from rest_framework.permissions import BasePermission


class isProfileTypeBusiness(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.profile.type == "business"
    

class isUserOfferCreator(BasePermission):

    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        user = request.user
        creator = obj.creator
        return user == creator