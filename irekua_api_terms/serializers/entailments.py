from irekua_terms.models import Entailment
from irekua_api_core.serializers import IrekuaModelSerializer
from .terms import TermSerializer
from .terms import TermDetailSerializer


class EntailmentSerializer(IrekuaModelSerializer):
    source = TermSerializer(read_only=True)

    target = TermSerializer(read_only=True)

    class Meta:
        model = Entailment

        fields = (
            'id',
            'url',
            'source',
            'target',
            'metadata',
        )


class EntailmentDetailSerializer(IrekuaModelSerializer):
    source = TermDetailSerializer(read_only=True)

    target = TermDetailSerializer(read_only=True)

    class Meta:
        model = Entailment

        fields = (
            'id',
            'source',
            'target',
            'metadata',
        )
