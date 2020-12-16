from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import Collection
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = Collection.objects.all()

    serializer_class = serializers.CollectionSerializer

    filterset_class = filters.collections.Filter

    search_fields = filters.collections.search_fields

    ordering_fields = filters.collections.ordering_fields
