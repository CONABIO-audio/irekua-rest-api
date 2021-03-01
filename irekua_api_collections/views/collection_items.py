from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionItem
from irekua_collections import filters

from irekua_api_collections import serializers
from irekua_api_collections.permissions import CanViewItem
from irekua_api_collections.permissions import CanCreateItem
from irekua_api_collections.permissions import CanUpdateItem
from irekua_api_collections.permissions import CanDeleteItem


class CollectionItemViewSet(IrekuaModelViewSet):
    serializer_class = serializers.CollectionItemSerializer

    serializer_action_classes = {
        "validate": serializers.CollectionItemValidationSerializer
    }

    permission_action_classes = {
        "list": [IsAuthenticated],
        "create": [CanCreateItem],
        "validate": [IsAuthenticated],
        "retrieve": [CanViewItem],
        "update": [CanUpdateItem],
        "partial_update": [CanUpdateItem],
        "destroy": [CanDeleteItem],
    }

    filterset_class = filters.collection_items.Filter

    search_fields = filters.collection_items.search_fields

    ordering_fields = filters.collection_items.ordering_fields

    def get_queryset(self):
        return CollectionItem.objects.can_view(self.request.user)

    @action(detail=False, methods=["post"])
    def validate(self, request):
        serializer = serializers.CollectionItemValidationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        return Response({}, status=200)
