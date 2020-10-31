from irekua_terms.models import TermType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_terms import serializers
from irekua_api_terms import filters


class TermTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = TermType.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.TermTypeDetailSerializer
    }

    serializer_class = serializers.TermTypeSerializer

    filterset_class = filters.term_types.Filter

    search_fields = filters.term_types.search_fields

    ordering_fields = filters.term_types.ordering_fields
