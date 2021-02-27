from rest_framework.permissions import BasePermission


class CanViewItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_special:
            return True

        if obj.created_by == user:
            return True

        # Check if licence allows all users to see the item
        licence = obj.licence
        if not licence.is_active:
            # If the licence is overdue then all users can view the
            # item
            return True

        if licence.licence_type.can_view_items:
            # If it's an open licence allow all users to view
            return True

        # If licence does not permit public access then delegate
        # the permission granting to the collection
        collection = obj.collection
        return collection.has_permission(user, "view_collectionitem")


class CanUpdateItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_superuser or user.is_curator:
            return True

        if obj.created_by == user:
            return True

        collection = obj.collection
        return collection.has_permission(user, "change_collectionitem")


class CanDeleteItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_superuser or user.is_curator:
            return True

        if obj.created_by == user:
            return True

        collection = obj.collection
        return collection.has_permission(user, "delete_collectionitem")