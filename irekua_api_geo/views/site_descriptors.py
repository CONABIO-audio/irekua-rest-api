from irekua_geo.models import SiteDescriptor
from irekua_geo import filters

from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_geo import serializers


class SiteDescriptorViewSet(IrekuaReadOnlyViewSet):
    queryset = SiteDescriptor.objects.all()

    serializer_class = serializers.SiteDescriptorSerializer

    serializer_action_classes = {"retrieve": serializers.SiteDescriptorDetailSerializer}

    filterset_class = filters.site_descriptors.Filter

    search_fields = filters.site_descriptors.search_fields

    ordering_fields = filters.site_descriptors.ordering_fields
