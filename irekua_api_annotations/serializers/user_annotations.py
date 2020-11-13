from irekua_annotations.models import UserAnnotation
from .annotations import AnnotationSerializer
from .annotations import AnnotationDetailSerializer


class UserAnnotationSerializer(AnnotationSerializer):
    class Meta(AnnotationSerializer.Meta):
        model = UserAnnotation

        fields = (
            *AnnotationSerializer.Meta.fields,
            "certainty",
            "quality",
        )


class UserAnnotationDetailSerializer(AnnotationDetailSerializer):
    class Meta(AnnotationDetailSerializer.Meta):
        model = UserAnnotation

        fields = (
            *AnnotationDetailSerializer.Meta.fields,
            "certainty",
            "quality",
            "commentaries",
        )
