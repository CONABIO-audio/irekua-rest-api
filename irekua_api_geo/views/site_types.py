from irekua_geo.models import SiteType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_geo import serializers
from irekua_api_geo import filters


class SiteTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = SiteType.objects.all()

    serializer_class = serializers.SiteTypeSerializer

    serializer_action_classes = {"retrieve": serializers.SiteTypeDetailSerializer}

    filterset_class = filters.site_types.Filter

    search_fields = filters.site_types.search_fields

    ordering_fields = filters.site_types.ordering_fields
