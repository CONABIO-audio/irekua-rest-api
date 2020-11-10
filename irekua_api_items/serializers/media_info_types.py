from rest_framework import serializers

from irekua_items.models import MediaInfoType
from irekua_api_schemas.serializers import SchemaSerializer


class MediaInfoTypeSerializer(serializers.ModelSerializer):
    media_info_schema = SchemaSerializer(read_only=True)

    class Meta:
        model = MediaInfoType
        fields = (
            'name',
            'description',
            'media_info_schema',
        )
