from irekua_items.models import Item
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import SpecialOnly
from irekua_api_items import serializers
from irekua_api_items import filters


class ItemViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [SpecialOnly]

    queryset = Item.objects.all()

    serializer_class = serializers.ItemSerializer

    serializer_action_classes = {
        'retrieve': serializers.ItemDetailSerializer
    }

    filterset_class = filters.items.Filter

    search_fields = filters.items.search_fields

    ordering_fields = filters.items.ordering_fields
