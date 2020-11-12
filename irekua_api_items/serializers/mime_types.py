from rest_framework import serializers

from irekua_items.models import MimeType

from irekua_api_schemas.serializers import SchemaSerializer
from irekua_api_schemas.serializers import SchemaDetailSerializer


class MimeTypeSerializer(serializers.ModelSerializer):
    media_info_schema = SchemaSerializer(read_only=True)

    class Meta:
        model = MimeType
        fields = (
            "mime_type",
            "media_info_schema",
        )


class MimeTypeDetailSerializer(serializers.ModelSerializer):
    media_info_schema = SchemaDetailSerializer(read_only=True)

    class Meta(MimeTypeSerializer.Meta):
        pass
