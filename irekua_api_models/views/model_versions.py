from irekua_models import filters
from irekua_models.models import ModelVersion

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper
from irekua_api_models import serializers


class ModelVersionViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = ModelVersion.objects.all()

    serializer_class = serializers.ModelVersionDetailSerializer

    serializer_action_classes = {"create": serializers.ModelVersionCreateSerializer}

    filterset_class = filters.model_versions.Filter

    search_fields = filters.model_versions.search_fields

    ordering_fields = filters.model_versions.ordering_fields
