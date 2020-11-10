from irekua_geo.models import Locality
from irekua_api_core.serializers import IrekuaModelSerializer

from .locality_types import LocalityTypeSerializer
from .locality_types import LocalityTypeDetailSerializer


class LocalitySerializer(IrekuaModelSerializer):
    locality_type = LocalityTypeSerializer(read_only=True)

    class Meta:
        model = Locality

        fields = (
            'url',
            'id',
            'name',
            'description',
            'locality_type',
            'created_on',
        )


class LocalityDetailSerializer(IrekuaModelSerializer):
    locality_type = LocalityTypeDetailSerializer(read_only=True)

    is_part_of = LocalitySerializer(read_only=True, many=True)

    class Meta(LocalitySerializer.Meta):
        fields = (
            *LocalitySerializer.Meta.fields,
            'metadata',
            'geometry',
            'modified_on',
            'is_part_of',
        )
