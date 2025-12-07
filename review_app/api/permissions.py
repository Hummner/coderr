from rest_framework.permissions import BasePermission


class IsUserCustomer(BasePermission):
    """
    Permission class that restricts certain actions—such as creating a review—
    to users whose profile type is 'customer'. This ensures only customers can
    submit feedback for business users.
    """

    def has_permission(self, request, view):
        """
        Grant permission only if the authenticated user is registered
        as a customer within their profile.
        """
        return request.user.profile.type == "customer"
    

class IsReviewOwner(BasePermission):
    """
    Permission class ensuring that only the creator of a review is allowed
    to update or delete it. This prevents users from modifying reviews that
    do not belong to them.
    """

    def has_object_permission(self, request, view, obj):
        """
        Grant object-level permission only when the requesting user is
        the review owner.
        """
        owner = obj.reviewer
        user = request.user
        return owner == user
