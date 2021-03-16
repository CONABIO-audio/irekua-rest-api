from irekua_terms.models import Term
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_terms import serializers
from irekua_terms import filters


class TermViewSet(IrekuaReadOnlyViewSet):
    queryset = Term.objects.all()

    serializer_action_classes = {"retrieve": serializers.TermComplexSerializer}

    serializer_class = serializers.TermSerializer

    filterset_class = filters.terms.Filter

    search_fields = filters.terms.search_fields

    ordering_fields = filters.terms.ordering_fields
