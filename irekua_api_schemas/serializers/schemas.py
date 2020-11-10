from irekua_schemas.models import Schema

from irekua_api_core.serializers import IrekuaModelSerializer


class SchemaSerializer(IrekuaModelSerializer):
    class Meta:
        model = Schema

        fields = (
            'url',
            'id',
            'name',
            'description',

        )


class SchemaDetailSerializer(IrekuaModelSerializer):
    class Meta(SchemaSerializer.Meta):
        fields = (
            *SchemaSerializer.Meta.fields,
            'schema',
            'created_on',
            'modified_on',
        )
