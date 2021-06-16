from irekua_visualizers.models import VisualizerModule
from irekua_api_core.serializers import IrekuaModelSerializer

from .visualizer_versions import VisualizerVersionSerializer


class VisualizerModuleSerializer(IrekuaModelSerializer):
    visualizer_version = VisualizerVersionSerializer(read_only=True)

    class Meta:
        model = VisualizerModule
        fields = (
            "url",
            "id",
            "visualizer_version",
            "javascript_file",
            "is_active"
        )
