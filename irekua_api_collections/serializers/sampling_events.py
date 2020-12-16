from irekua_collections.models import SamplingEvent
from irekua_api_core.serializers import IrekuaUserModelSerializer


class SamplingEventSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = SamplingEvent

        fields = (
            "id",
            "url",
            "collection",
            "collection_site",
            "sampling_event_type",
            "started_on",
            "ended_on",
            "metadata",
            "collection_metadata",
            "commentaries",
            "created_on",
            "created_by",
        )
