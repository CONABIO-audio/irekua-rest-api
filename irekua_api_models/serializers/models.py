from rest_framework import serializers

from irekua_models.models import Model
from irekua_api_core.serializers import IrekuaModelSerializer


class ModelDetailSerializer(IrekuaModelSerializer):
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


class ModelCreateSerializer(IrekuaModelSerializer):
    class Meta:
        model = Model

        fields = (
            "name",
            "description",
            "repository",
            "annotation_type",
        )
