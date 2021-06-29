
from rest_framework.decorators import action
from rest_framework.response import Response

from irekua_visualizers import filters
from irekua_visualizers.models import VisualizerModule
from irekua_visualizers.models import VisualizerVersion
from irekua_visualizers.models import Visualizer

from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.permissions import IsSuperuser
from irekua_api_core.permissions import IsDeveloper
from irekua_api_visualizers import serializers


class VisualizerModuleViewSet(IrekuaModelViewSet):
    permission_classes = [IsAuthenticated]

    permission_action_classes = {
        "create": [IsSuperuser | IsDeveloper],
        "update": [IsSuperuser | IsDeveloper],
        "partial_update": [IsSuperuser | IsDeveloper],
        "destroy": [IsSuperuser | IsDeveloper],
    }

    queryset = VisualizerModule.objects.all()

    serializer_class = serializers.VisualizerModuleSerializer

    filterset_class = filters.visualizer_modules.Filter

    search_fields = filters.visualizer_modules.search_fields

    ordering_fields = filters.visualizer_modules.ordering_fields

    @action(detail=False, methods=["get"])
    def item_type_visualizer(self, request, item_type=None):
        version = VisualizerModule.objects.filter(
                visualizer_version__visualizer__item_types__id=request.GET['item_type'],
                is_active=True).first()

        response_data = {
            'javascript_file': version.javascript_file.url,
        }

        return Response(response_data, status=200)
