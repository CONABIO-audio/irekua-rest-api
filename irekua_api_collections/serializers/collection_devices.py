from irekua_collections.models import CollectionDevice
from irekua_api_core.serializers import IrekuaUserModelSerializer


class CollectionDeviceSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = CollectionDevice

        fields = (
            "id",
            "url",
            "collection",
            "physical_device",
            "collection_metadata",
            "collection_name",
            "created_on",
            "created_by",
        )
