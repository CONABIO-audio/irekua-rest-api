from irekua_geo.models import Locality
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_geo import serializers
from irekua_geo import filters


class LocalityViewSet(IrekuaReadOnlyViewSet):
    queryset = Locality.objects.all()

    serializer_class = serializers.LocalitySerializer

    serializer_action_classes = {"retrieve": serializers.LocalityDetailSerializer}

    filterset_class = filters.localities.Filter

    search_fields = filters.localities.search_fields

    ordering_fields = filters.localities.ordering_fields
