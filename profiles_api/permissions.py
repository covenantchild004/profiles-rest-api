from rest_framework import permissions


class UpdateownProfile(permissions.BasePermission):
    """Allow user to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
