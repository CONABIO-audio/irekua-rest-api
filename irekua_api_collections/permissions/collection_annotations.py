from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


from irekua_collections.models import Collection


class CanCreateAnnotation(IsAuthenticated):
    def has_permission(self, request, view):
        collection_pk = request.POST.get("collection", None)

        if collection_pk is None:
            return False

        try:
            collection = Collection.objects.get(pk=collection_pk)
            return collection.can_create_annotation(request.user)

        except Collection.DoesNotExist:
            return False


class CanViewAnnotation(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_view(request.user)


class CanUpdateAnnotation(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_change(request.user)


class CanDeleteAnnotation(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_delete(request.user)


class CanVoteAnnotation(AllowAny):
    def has_object_permission(self, request, view, obj):
        return obj.can_vote(request.user)
