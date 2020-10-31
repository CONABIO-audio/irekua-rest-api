from irekua_terms.models import Term
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_terms import serializers
from irekua_api_terms import filters


class TermViewSet(IrekuaReadOnlyViewSet):
    queryset = Term.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.TermDetailSerializer
    }

    serializer_class = serializers.TermSerializer
