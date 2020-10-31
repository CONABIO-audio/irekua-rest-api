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
            'created_on',
        )

        # extra_kwargs = {
        #     'url': {
        #         'view_name': 'irekua_api_schemas:schema-detail'
        #     },
        # }


class SchemaDetailSerializer(IrekuaModelSerializer):
    class Meta(SchemaSerializer.Meta):
        fields = (
            *SchemaSerializer.Meta.fields,
            'schema',
            'modified_on',
        )
