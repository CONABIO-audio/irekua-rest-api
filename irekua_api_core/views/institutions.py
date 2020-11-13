from irekua_database.models import Institution
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_core import serializers
from irekua_database.filters import institutions as filters


class InstitutionViewSet(IrekuaReadOnlyViewSet):
    queryset = Institution.objects.all()

    serializer_class = serializers.InstitutionSerializer

    filterset_class = filters.Filter

    search_fields = filters.search_fields

    ordering_fields = filters.ordering_fields
