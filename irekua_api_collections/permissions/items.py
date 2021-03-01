from rest_framework.permissions import BasePermission

from irekua_collections.models import Collection


class CanCreateItem(BasePermission):
    def has_permission(self, request, view):
        collection_pk = request.GET.get("collection", None)

        if collection_pk is None:
            return False

        collection = Collection.objects.get(pk=collection_pk)
        return collection.can_add_items(request.user)


class CanViewItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.can_view(request.user)


class CanUpdateItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.can_update(request.user)


class CanDeleteItem(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.can_delete(request.user)
