from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


from irekua_collections.models import Collection


class CanCreateItem(IsAuthenticated):
    def has_permission(self, request, view):
        collection_pk = request.GET.get("collection", None)

        if collection_pk is None:
            return False

        collection = Collection.objects.get(pk=collection_pk)
        return collection.can_add_items(request.user)


class CanViewItem(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_view(request.user)


class CanUpdateItem(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_change(request.user)


class CanDeleteItem(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_delete(request.user)
