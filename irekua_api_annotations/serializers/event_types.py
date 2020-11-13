from irekua_annotations.models import EventType
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_schemas.serializers import SchemaSerializer
from irekua_api_terms.serializers import TermSerializer
from irekua_api_terms.serializers import TermTypeSerializer
from irekua_api_items.serializers import ItemTypeSerializer
from .annotation_types import AnnotationTypeSerializer


class EventTypeSerializer(IrekuaModelSerializer):
    term_types = TermTypeSerializer(many=True, read_only=True)

    should_imply = TermSerializer(many=True, read_only=True)

    item_types = ItemTypeSerializer(many=True, read_only=True)

    annotation_types = AnnotationTypeSerializer(many=True, read_only=True)

    class Meta:
        model = EventType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "term_types",
            "should_imply",
            "item_types",
            "restrict_annotation_types",
            "annotation_types",
        )


class EventTypeDetailSerializer(EventTypeSerializer):
    metadata_schema = SchemaSerializer(read_only=True)

    class Meta(EventTypeSerializer.Meta):
        fields = (
            *EventTypeSerializer.Meta.fields,
            "metadata_schema",
            "created_on",
            "modified_on",
        )
