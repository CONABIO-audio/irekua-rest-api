from irekua_models.models import ModelPrediction
from irekua_api_core.views import IrekuaModelViewSet

from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper

from irekua_api_models import serializers
from irekua_models import filters


class ModelPredictionViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = ModelPrediction.objects.all()

    serializer_class = serializers.ModelPredictionDetailSerializer

    serializer_action_classes = {
        "create": serializers.ModelPredictionCreateSerializer
    }

    filterset_class = filters.model_predictions.Filter

    search_fields = filters.model_predictions.search_fields

    ordering_fields = filters.model_predictions.ordering_fields
