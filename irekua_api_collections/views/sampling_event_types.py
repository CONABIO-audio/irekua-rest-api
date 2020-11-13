from irekua_collections.models import SamplingEventType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_collections import serializers
from irekua_api_collections import filters


class SamplingEventTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = SamplingEventType.objects.all()

    serializer_class = serializers.SamplingEventTypeSerializer

    serializer_action_classes = {
        "retrieve": serializers.SamplingEventTypeDetailSerializer
    }

    filterset_class = filters.sampling_event_types.Filter

    search_fields = filters.sampling_event_types.search_fields

    ordering_fields = filters.sampling_event_types.ordering_fields
