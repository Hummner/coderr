from rest_framework.permissions import BasePermission


class ProfilePatchPermission(BasePermission):
    """
    Permission class that ensures only the owner of a profile is allowed to
    update it. This prevents users from modifying other users' profile data.
    """

    def has_object_permission(self, request, view, obj):
        """
        Grant permission only if the authenticated user is the same user
        associated with the profile object being updated.
        """
        user = request.user
        return obj.user == user
