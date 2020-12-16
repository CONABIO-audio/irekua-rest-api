from irekua_models.models import Model
from irekua_api_core.serializers import IrekuaUserModelSerializer


class ModelDetailSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Model

        fields = (
            "url",
            "id",
            "name",
            "description",
            "repository",
            "annotation_type",
            "item_types",
            "event_types",
            "terms",
        )


class ModelCreateSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Model

        fields = (
            "name",
            "description",
            "repository",
            "annotation_type",
        )
