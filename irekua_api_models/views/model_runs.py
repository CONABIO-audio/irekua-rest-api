from irekua_models.models import ModelRun
from irekua_api_core.views import IrekuaModelViewSet

from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper
from irekua_api_models import serializers
from irekua_models import filters


class ModelRunViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = ModelRun.objects.all()

    serializer_class = serializers.ModelRunDetailSerializer

    serializer_action_classes = {"create": serializers.ModelRunCreateSerializer}

    filterset_class = filters.model_runs.Filter

    search_fields = filters.model_runs.search_fields

    ordering_fields = filters.model_runs.ordering_fields
