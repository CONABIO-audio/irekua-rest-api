from irekua_annotations.models import Annotation
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_core.serializers import IrekuaUserModelSerializer


class AnnotationSerializer(IrekuaModelSerializer):
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


class AnnotationCreateSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Annotation

        fields = (
            "item",
            "annotation_type",
            "event_type",
            "annotation",
            "labels",
            "annotation_metadata",
            "event_metadata",
        )