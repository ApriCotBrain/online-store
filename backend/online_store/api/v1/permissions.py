"""Permissions for the endpoints of 'Api' application v1."""

from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwner(BasePermission):
    """Requests are allowed are allowed only to the owner."""

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
