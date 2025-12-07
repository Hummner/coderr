from rest_framework.permissions import BasePermission


class isProfileTypeBusiness(BasePermission):
    """
    Permission class ensuring that only users whose profile type is 'business'
    are allowed to perform the requested action. Used for limiting offer creation
    to business accounts.
    """

    def has_permission(self, request, view):
        """
        Grant permission only if the authenticated user's profile type
        is set to 'business'.
        """
        user = request.user
        return user.profile.type == "business"
    

class isUserOfferCreator(BasePermission):
    """
    Permission class that allows access only to the creator of a specific offer.
    Used to restrict destructive or modifying actions such as deletion.
    """

    def has_permission(self, request, view):
        """
        Allow the request to continue to object-level permission checks.
        Always returns the default BasePermission behavior.
        """
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        """
        Grant permission only if the user making the request is the same
        user who originally created the offer instance.
        """
        user = request.user
        creator = obj.creator
        return user == creator
