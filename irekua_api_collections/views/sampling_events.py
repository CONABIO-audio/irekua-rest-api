from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import SamplingEvent
from irekua_collections import filters
from irekua_api_collections import serializers


class SamplingEventViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = SamplingEvent.objects.all()

    serializer_class = serializers.SamplingEventSerializer

    filterset_class = filters.sampling_events.Filter

    search_fields = filters.sampling_events.search_fields

    ordering_fields = filters.sampling_events.ordering_fields
