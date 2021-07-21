from irekua_geo.models import Locality
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.views import IrekuaModelViewSet

from irekua_api_geo import serializers
from irekua_geo import filters


class LocalityViewSet(IrekuaModelViewSet):
    queryset = Locality.objects.all()    
    
    permission_action_classes = {
        "create": [IsAuthenticated],
    }

    serializer_class = serializers.LocalitySerializer

    serializer_action_classes = {
        "retrieve": serializers.LocalityDetailSerializer,
        "create": serializers.LocalityCreateSerializer
    }

    filterset_class = filters.localities.Filter

    search_fields = filters.localities.search_fields

    ordering_fields = filters.localities.ordering_fields
