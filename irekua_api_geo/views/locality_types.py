from irekua_geo.models import LocalityType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_geo import serializers
from irekua_geo import filters


class LocalityTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = LocalityType.objects.all()

    serializer_class = serializers.LocalityTypeSerializer

    serializer_action_classes = {
        'retrieve': serializers.LocalityTypeDetailSerializer
    }

    filterset_class = filters.locality_types.Filter

    search_fields = filters.locality_types.search_fields

    ordering_fields = filters.locality_types.ordering_fields
