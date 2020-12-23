from rest_framework.response import Response
from rest_framework.decorators import action

from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionItem
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionItemViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = CollectionItem.objects.all()

    serializer_class = serializers.CollectionItemSerializer

    serializer_action_classes = {
        "validate": serializers.CollectionItemValidationSerializer
    }

    filterset_class = filters.collection_items.Filter

    search_fields = filters.collection_items.search_fields

    ordering_fields = filters.collection_items.ordering_fields

    def get_queryset(self):
        return CollectionItem.objects.all()

    @action(detail=False, methods=["post"])
    def validate(self, request):
        serializer = serializers.CollectionItemValidationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        return Response({}, status=200)
