from irekua_annotations.models import Annotation
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_terms.serializers import TermSerializer
from irekua_api_items.serializers import ItemSerializer
from .annotation_types import AnnotationTypeSerializer
from .event_types import EventTypeSerializer


class AnnotationSerializer(IrekuaModelSerializer):
    item = ItemSerializer(read_only=True)

    annotation_type = AnnotationTypeSerializer(read_only=True)

    event_type = EventTypeSerializer(read_only=True)

    labels = TermSerializer(read_only=True, many=True)

    class Meta:
        model = Annotation

        fields = (
            "url",
            "id",
            "item",
            "annotation_type",
            "event_type",
            "annotation",
            "labels",
            "created_on",
            "created_by",
        )


class AnnotationDetailSerializer(AnnotationSerializer):
    class Meta(AnnotationSerializer.Meta):
        fields = (
            *AnnotationSerializer.Meta.fields,
            "annotation_metadata",
            "event_metadata",
            "modified_on",
            "modified_by",
        )
