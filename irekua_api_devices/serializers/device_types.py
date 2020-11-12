from irekua_devices.models import DeviceType
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_items.serializers import MimeTypeSerializer


class DeviceTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = DeviceType

        fields = (
            "url",
            "id",
            "name",
            "icon",
        )


class DeviceTypeDetailSerializer(IrekuaModelSerializer):
    mime_types = MimeTypeSerializer(many=True, read_only=True)

    class Meta(DeviceTypeSerializer.Meta):
        fields = (
            *DeviceTypeSerializer.Meta.fields,
            "mime_types",
            "created_on",
            "modified_on",
        )
