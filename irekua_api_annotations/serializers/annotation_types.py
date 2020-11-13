from irekua_annotations.models import AnnotationType
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_schemas.serializers import SchemaSerializer


class AnnotationTypeSerializer(IrekuaModelSerializer):
    annotation_schema = SchemaSerializer(read_only=True)

    class Meta:
        model = AnnotationType

        fields = ("url", "id", "name", "description", "icon", "annotation_schema")


class AnnotationTypeDetailSerializer(IrekuaModelSerializer):
    annotation_schema = SchemaSerializer(read_only=True)

    metadata_schema = SchemaSerializer(read_only=True)

    class Meta(AnnotationTypeSerializer.Meta):
        fields = (
            *AnnotationTypeSerializer.Meta.fields,
            "metadata_schema",
            "created_on",
            "modified_on",
        )
