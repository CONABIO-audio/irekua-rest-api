from irekua_collections.models import DeploymentType

from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_items.serializers import ItemTypeSerializer
from irekua_api_devices.serializers import DeviceTypeSerializer
from irekua_api_schemas.serializers import SchemaSerializer


class DeploymentTypeSerializer(IrekuaModelSerializer):
    item_types = ItemTypeSerializer(many=True, read_only=True)

    device_type = DeviceTypeSerializer(read_only=True)

    class Meta:
        model = DeploymentType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "device_type",
            "restrict_item_types",
            "item_types",
        )


class DeploymentTypeDetailSerializer(IrekuaModelSerializer):
    metadata_schema = SchemaSerializer(read_only=True)

    class Meta(DeploymentTypeSerializer.Meta):
        fields = (
            *DeploymentTypeSerializer.Meta.fields,
            "metadata_schema",
            "created_on",
            "modified_on",
        )
