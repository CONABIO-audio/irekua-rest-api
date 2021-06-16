from irekua_visualizers import filters
from irekua_visualizers.models import Visualizer

from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsDeveloper
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_visualizers import serializers


class VisualizersViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = Visualizer.objects.all()

    serializer_class = serializers.VisualizerSerializer

    filterset_class = filters.visualizers.Filter

    search_fields = filters.visualizers.search_fields

    ordering_fields = filters.visualizers.ordering_fields
