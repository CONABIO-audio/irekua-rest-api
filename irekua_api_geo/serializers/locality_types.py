from irekua_geo.models import LocalityType
from irekua_api_core.serializers import IrekuaModelSerializer


class LocalityTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = LocalityType

        fields = (
            'url',
            'id',
            'name',
        )


class LocalityTypeDetailSerializer(IrekuaModelSerializer):
    class Meta(LocalityTypeSerializer.Meta):
        fields = (
            *LocalityTypeSerializer.Meta.fields,
            'description',
            'source',
            'original_datum',
            'publication_date',
            'created_on',
            'modified_on',
        )
