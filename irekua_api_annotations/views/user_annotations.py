from irekua_annotations.models import UserAnnotation
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_api_annotations import serializers
from irekua_annotations import filters


class UserAnnotationViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = UserAnnotation.objects.all()

    serializer_class = serializers.UserAnnotationSerializer

    serializer_action_classes = {"retrieve": serializers.UserAnnotationDetailSerializer}

    filterset_class = filters.user_annotations.Filter

    search_fields = filters.user_annotations.search_fields

    ordering_fields = filters.user_annotations.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return UserAnnotation.objects.none()

        if user.is_special:
            return UserAnnotation.objects.all()

        return UserAnnotation.objects.filter(created_by=user)
