from irekua_terms.models import Entailment
from irekua_api_core.serializers import IrekuaModelSerializer


class EntailmentSerializer(IrekuaModelSerializer):
    class Meta:
        model = Entailment

        fields = (
            'id',
        )


class EntailmentDetailSerializer(IrekuaModelSerializer):
    class Meta:
        model = Entailment

        fields = (
            'id',
        )
