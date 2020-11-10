from irekua_terms.models import TermType
from irekua_api_schemas.serializers import SchemaDetailSerializer
from irekua_api_core.serializers import IrekuaModelSerializer


class TermTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = TermType

        fields = (
            'url',
            'id',
            'name',
            'description',
            'is_categorical',
            'is_numerical',
            'is_boolean',
            'is_integer',
            'created_on',
        )


class TermTypeDetailSerializer(IrekuaModelSerializer):
    entailments = TermTypeSerializer(
        many=True,
        read_only=True,
    )

    metadata_schema = SchemaDetailSerializer(
        read_only=True,
    )

    synonym_metadata_schema = SchemaDetailSerializer(
        read_only=True,
    )

    class Meta(TermTypeSerializer.Meta):
        fields = (
            *TermTypeSerializer.Meta.fields,
            'metadata_schema',
            'synonym_metadata_schema',
            'entailments',
        )
