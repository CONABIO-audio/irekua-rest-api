from irekua_items.models import ItemType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_items import serializers
from irekua_api_items import filters


class ItemTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = ItemType.objects.all()

    serializer_class = serializers.ItemTypeSerializer

    filterset_class = filters.item_types.Filter

    search_fields = filters.item_types.search_fields

    ordering_fields = filters.item_types.ordering_fields
