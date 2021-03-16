from irekua_items.models import ItemType
from irekua_api_core.serializers import IrekuaModelSerializer

from .media_info_types import MediaInfoTypeSerializer
from .mime_types import MimeTypeSerializer


class ItemTypeSerializer(IrekuaModelSerializer):
    media_info_type = MediaInfoTypeSerializer(read_only=True)
    mime_types = MimeTypeSerializer(read_only=True, many=True)

    class Meta:
        model = ItemType

        fields = (
            "url",
            "id",
            "name",
            "media_info_type",
            "mime_types",
        )
