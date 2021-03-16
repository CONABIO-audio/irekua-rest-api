from irekua_models.models import ModelVersion
from irekua_api_core.serializers import IrekuaUserModelSerializer


class ModelVersionDetailSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = ModelVersion

        fields = (
            "url",
            "id",
            "model",
            "version",
            "created_by",
            "created_on",
        )


class ModelVersionCreateSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = ModelVersion

        fields = (
            "model",
            "version",
        )
