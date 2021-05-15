from irekua_models import filters
from irekua_models.models import Model

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper
from irekua_api_models import serializers


class ModelViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = Model.objects.all()

    serializer_class = serializers.ModelDetailSerializer

    filterset_class = filters.models.Filter

    search_fields = filters.models.search_fields

    ordering_fields = filters.models.ordering_fields
