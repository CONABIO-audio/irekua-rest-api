from irekua_devices.models import Device
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_devices import serializers
from irekua_devices import filters


class DeviceViewSet(IrekuaReadOnlyViewSet):
    queryset = Device.objects.all()

    serializer_class = serializers.DeviceSerializer

    serializer_action_classes = {"retrieve": serializers.DeviceDetailSerializer}

    filterset_class = filters.devices.Filter

    search_fields = filters.devices.search_fields

    ordering_fields = filters.devices.ordering_fields
