from irekua_geo.models import SiteDescriptorType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_geo import serializers
from irekua_geo import filters


class SiteDescriptorTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = SiteDescriptorType.objects.all()

    serializer_class = serializers.SiteDescriptorTypeSerializer

    serializer_action_classes = {
        "retrieve": serializers.SiteDescriptorTypeDetailSerializer
    }

    filterset_class = filters.site_descriptor_types.Filter

    search_fields = filters.site_descriptor_types.search_fields

    ordering_fields = filters.site_descriptor_types.ordering_fields
