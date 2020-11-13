from irekua_terms.models import Entailment
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_terms import serializers
from irekua_terms import filters


class EntailmentViewSet(IrekuaReadOnlyViewSet):
    queryset = Entailment.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.EntailmentDetailSerializer
    }

    serializer_class = serializers.EntailmentSerializer

    filterset_class = filters.entailments.Filter

    search_fields = filters.entailments.search_fields

    ordering_fields = filters.entailments.ordering_fields
