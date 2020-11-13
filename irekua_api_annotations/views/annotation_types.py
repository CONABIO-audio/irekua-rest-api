from irekua_annotations.models import AnnotationType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_annotations import serializers
from irekua_api_annotations import filters


class AnnotationTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = AnnotationType.objects.all()

    serializer_class = serializers.AnnotationTypeSerializer

    serializer_action_classes = {"retrieve": serializers.AnnotationTypeDetailSerializer}

    filterset_class = filters.annotation_types.Filter

    search_fields = filters.annotation_types.search_fields

    ordering_fields = filters.annotation_types.ordering_fields
