from irekua_visualizers import filters
from irekua_visualizers.models import VisualizerVersion

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper
from irekua_api_visualizers import serializers


class VisualizerVersionViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = VisualizerVersion.objects.all()

    serializer_class = serializers.VisualizerVersionSerializer
