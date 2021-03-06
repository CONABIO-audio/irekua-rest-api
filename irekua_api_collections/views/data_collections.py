from rest_framework.decorators import action
from rest_framework.response import Response

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.serializers import RoleSerializer

from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner
from irekua_api_core.permissions import IsAuthenticated

from irekua_collections.models import Collection
from irekua_collections import filters

from irekua_api_collections import serializers
from irekua_api_collections.permissions import CanViewCollection
from irekua_api_collections.permissions import CanCreateCollection
from irekua_api_collections.permissions import CanUpdateCollection
from irekua_api_collections.permissions import CanDeleteCollection


class CollectionViewSet(IrekuaModelViewSet):
    permission_action_classes = {
        "list": [IsAuthenticated],
        "create": [CanCreateCollection],
        "retrieve": [CanViewCollection],
        "update": [CanUpdateCollection],
        "partial_update": [CanUpdateCollection],
        "destroy": [CanDeleteCollection],
    }

    serializer_class = serializers.CollectionSerializer

    filterset_class = filters.collections.Filter

    search_fields = filters.collections.search_fields

    ordering_fields = filters.collections.ordering_fields

    def get_queryset(self):
        return Collection.objects.can_view(self.request.user)

    @action(detail=True, methods=["get"])
    def role(self, request, pk=None):
        collection = self.get_object()

        role = collection.get_user_role(request.user)

        if role is None:
            return Response("You are not a user of this collection", status=404)

        serializer = RoleSerializer(role)
        return Response(serializer.data, status=200)
