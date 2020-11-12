from irekua_devices.models import DeviceType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_devices import serializers
from irekua_api_devices import filters


class DeviceTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = DeviceType.objects.all()

    serializer_class = serializers.DeviceTypeSerializer

    serializer_action_classes = {"retrieve": serializers.DeviceTypeDetailSerializer}

    filterset_class = filters.device_types.Filter

    search_fields = filters.device_types.search_fields

    ordering_fields = filters.device_types.ordering_fields
