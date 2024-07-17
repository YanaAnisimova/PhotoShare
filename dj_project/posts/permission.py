from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Object-level permission to only allow owner to edit objects.

    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """Object-level permission to only allow owner or admin.

    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
