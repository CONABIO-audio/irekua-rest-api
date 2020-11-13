from irekua_items.models import LicenceType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_items import serializers
from irekua_items import filters


class LicenceTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = LicenceType.objects.all()

    serializer_class = serializers.LicenceTypeSerializer

    filterset_class = filters.licence_types.Filter

    search_fields = filters.licence_types.search_fields

    ordering_fields = filters.licence_types.ordering_fields
