from irekua_items.models import Item
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner
from irekua_api_items import serializers
from irekua_api_items import filters


class ItemViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = Item.objects.all()

    serializer_class = serializers.ItemSerializer

    serializer_action_classes = {"retrieve": serializers.ItemDetailSerializer}

    filterset_class = filters.items.Filter

    search_fields = filters.items.search_fields

    ordering_fields = filters.items.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Item.objects.none()

        if user.is_special:
            return Item.objects.all()

        return Item.objects.filter(created_by=user)
