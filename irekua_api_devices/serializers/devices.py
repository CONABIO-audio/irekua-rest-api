from irekua_devices.models import Device
from irekua_api_core.serializers import IrekuaModelSerializer

from .device_types import DeviceTypeSerializer
from .device_types import DeviceTypeDetailSerializer
from .device_brands import DeviceBrandSerializer


class DeviceSerializer(IrekuaModelSerializer):
    device_type = DeviceTypeSerializer(read_only=True)
    brand = DeviceBrandSerializer(read_only=True)

    class Meta:
        model = Device

        fields = (
            "url",
            "id",
            "model",
            "brand",
            "device_type",
        )


class DeviceDetailSerializer(IrekuaModelSerializer):
    device_type = DeviceTypeDetailSerializer(read_only=True)

    class Meta(DeviceSerializer.Meta):
        fields = (
            *DeviceSerializer.Meta.fields,
            "created_on",
            "modified_on",
        )
