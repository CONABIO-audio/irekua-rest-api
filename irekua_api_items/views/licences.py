from irekua_items.models import Licence
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_items import serializers
from irekua_items import filters


class LicenceViewSet(IrekuaReadOnlyViewSet):
    queryset = Licence.objects.all()

    serializer_class = serializers.LicenceSerializer

    serializer_action_classes = {"retrieve": serializers.LicenceDetailSerializer}

    filterset_class = filters.licences.Filter

    search_fields = filters.licences.search_fields

    ordering_fields = filters.licences.ordering_fields
