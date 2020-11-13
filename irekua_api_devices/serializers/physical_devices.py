from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from irekua_devices.models import Device
from irekua_devices.models import PhysicalDevice
from irekua_api_core.autocomplete import get_autocomplete_style
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_core.serializers import IrekuaUserModelSerializer
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


class PhysicalDeviceCreateSerializer(IrekuaUserModelSerializer):
    device = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        help_text=_("Brand and make of device"),
        style=get_autocomplete_style(name="device", model=Device),
    )

    class Meta(PhysicalDeviceSerializer.Meta):
        model = PhysicalDevice

        fields = (
            "name",
            "device",
            "serial_number",
        )
