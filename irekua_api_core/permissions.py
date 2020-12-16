from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated


__all__ = [
    "IsAuthenticated",
    "IsSpecial",
    "IsOwner",
]


class IsSpecial(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        return user.is_special


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        return user.is_developer


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        return user.is_superuser


class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_anonymous:
            return False

        return obj.created_by == user
