from irekua_geo.models import Site
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_geo import serializers
from irekua_api_geo import filters


class SiteViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = Site.objects.all()

    serializer_class = serializers.SiteSerializer

    filterset_class = filters.sites.Filter

    search_fields = filters.sites.search_fields

    ordering_fields = filters.sites.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Site.objects.none()

        if user.is_special:
            return Site.objects.all()

        return Site.objects.filter(created_by=user)
