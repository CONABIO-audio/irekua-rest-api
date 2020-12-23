from irekua_models.models import ModelPrediction
from irekua_api_annotations.serializers import AnnotationDetailSerializer
from irekua_api_annotations.serializers import AnnotationCreateSerializer


class ModelPredictionDetailSerializer(AnnotationDetailSerializer):
    class Meta(AnnotationDetailSerializer.Meta):
        model = ModelPrediction

        fields = (
            *AnnotationDetailSerializer.Meta.fields,
            "model_version",
            "model_run",
            "certainty",
        )


class ModelPredictionCreateSerializer(AnnotationCreateSerializer):
    class Meta(AnnotationCreateSerializer.Meta):
        model = ModelPrediction

        fields = (
            *AnnotationCreateSerializer.Meta.fields,
            "model_version",
            "model_run",
            "certainty",
        )
