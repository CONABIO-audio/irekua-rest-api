from rest_framework.permissions import BasePermission


class IsSpecial(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        return user.is_special


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_anonymous:
            return False

        return obj.created_by == user
