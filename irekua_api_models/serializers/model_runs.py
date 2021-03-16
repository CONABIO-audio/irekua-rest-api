from irekua_models.models import ModelRun
from irekua_api_core.serializers import IrekuaUserModelSerializer


class ModelRunDetailSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = ModelRun

        fields = (
            "url",
            "id",
            "model_version",
            "item",
            "created_on",
            "created_by",
        )


class ModelRunCreateSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = ModelRun

        fields = (
            "model_version",
            "item",
        )
