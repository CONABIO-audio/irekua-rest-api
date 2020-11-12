from irekua_devices.models import PhysicalDevice
from irekua_api_core.serializers import IrekuaModelSerializer
from .devices import DeviceSerializer
from .devices import DeviceDetailSerializer


class PhysicalDeviceSerializer(IrekuaModelSerializer):
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = PhysicalDevice

        fields = (
            "url",
            "id",
            "name",
            "device",
            "serial_number",
        )


class PhysicalDeviceDetailSerializer(IrekuaModelSerializer):
    device = DeviceDetailSerializer(read_only=True)

    class Meta(PhysicalDeviceSerializer.Meta):
        fields = (
            *PhysicalDeviceSerializer.Meta.fields,
            "metadata",
            "created_on",
            "modified_on",
        )
