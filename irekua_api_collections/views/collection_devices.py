from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionDevice
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionDeviceViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = CollectionDevice.objects.all()

    serializer_class = serializers.CollectionDeviceSerializer

    filterset_class = filters.collection_devices.Filter

    search_fields = filters.collection_devices.search_fields

    ordering_fields = filters.collection_devices.ordering_fields
