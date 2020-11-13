from irekua_annotations.models import Annotation
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_annotations import serializers
from irekua_annotations import filters


class AnnotationViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = Annotation.objects.all()

    serializer_class = serializers.AnnotationSerializer

    serializer_action_classes = {"retrieve": serializers.AnnotationDetailSerializer}

    filterset_class = filters.annotations.Filter

    search_fields = filters.annotations.search_fields

    ordering_fields = filters.annotations.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Annotation.objects.none()

        if user.is_special:
            return Annotation.objects.all()

        return Annotation.objects.filter(created_by=user)
