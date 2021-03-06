from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


from irekua_collections.models import CollectionType


class CanCreateCollection(IsAuthenticated):
    def has_permission(self, request, view):
        collection_type_pk = request.POST.get("collection_type", None)

        if collection_type_pk is None:
            return False

        try:
            collection_type = CollectionType.objects.get(pk=collection_type_pk)
            return collection_type.can_create_collection(request.user)

        except CollectionType.DoesNotExist:
            return False


class CanViewCollection(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_view(request.user)


class CanUpdateCollection(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_change(request.user)


class CanDeleteCollection(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_delete(request.user)
