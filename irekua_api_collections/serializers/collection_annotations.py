from irekua_collections.models import CollectionAnnotation

from irekua_api_annotations.serializers import UserAnnotationSerializer
from irekua_api_annotations.serializers import UserAnnotationDetailSerializer


class CollectionAnnotationSerializer(UserAnnotationSerializer):
    class Meta(UserAnnotationSerializer.Meta):
        model = CollectionAnnotation

        fields = (
            *UserAnnotationSerializer.Meta.fields,
            "collection",
        )


class CollectionAnnotationDetailSerializer(UserAnnotationDetailSerializer):
    class Meta(UserAnnotationDetailSerializer.Meta):
        model = CollectionAnnotation

        fields = (
            *UserAnnotationDetailSerializer.Meta.fields,
            "collection",
        )
