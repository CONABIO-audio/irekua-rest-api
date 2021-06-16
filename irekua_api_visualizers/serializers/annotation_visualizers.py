from irekua_visualizers.models import AnnotationVisualizer
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_annotations.serializers import AnnotationSerializer

from .visualizer_versions import VisualizerVersionSerializer

class AnnotationVisualizerSerializer(IrekuaModelSerializer):
    class Meta:
        model = AnnotationVisualizer

        fields = (
            "url",
            "id",
            "visualizer_configuration"
        )

class AnnotationVisualizerDetailSerializer(IrekuaModelSerializer):
    annotation = AnnotationSerializer(read_only=True)

    visualizer_version = VisualizerVersionSerializer(read_only=True)

    class Meta(AnnotationVisualizerSerializer.Meta):
        pass


