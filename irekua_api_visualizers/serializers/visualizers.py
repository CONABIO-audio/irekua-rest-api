from irekua_visualizers.models import Visualizer
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_items.serializers import ItemTypeSerializer


class VisualizerSerializer(IrekuaModelSerializer):
    item_types = ItemTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Visualizer
        fields = (
            "url",
            "id",
            "name",
            "website",
            "item_types"
        )
