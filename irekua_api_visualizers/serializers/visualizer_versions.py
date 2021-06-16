from irekua_visualizers.models import VisualizerVersion
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_schemas.serializers import SchemaSerializer

from .visualizers import VisualizerSerializer


class VisualizerVersionSerializer(IrekuaModelSerializer):
    visualizer = VisualizerSerializer(read_only=True)

    configuration_schema = SchemaSerializer(read_only=True)

    class Meta:
        model = VisualizerVersion
        fields = (
            "url",
            "id",
            "visualizer",
            "version",
            "configuration_schema"
        )
