from irekua_annotations.models import EventType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_annotations import serializers
from irekua_annotations import filters


class EventTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = EventType.objects.all()

    serializer_class = serializers.EventTypeSerializer

    serializer_action_classes = {"retrieve": serializers.EventTypeDetailSerializer}

    filterset_class = filters.event_types.Filter

    search_fields = filters.event_types.search_fields

    ordering_fields = filters.event_types.ordering_fields
