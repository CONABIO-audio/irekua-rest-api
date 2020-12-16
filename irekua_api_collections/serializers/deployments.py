from irekua_collections.models import Deployment
from irekua_api_core.serializers import IrekuaUserModelSerializer


class DeploymentSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Deployment

        fields = (
            "id",
            "url",
            "sampling_event",
            "collection_device",
            "deployment_type",
            "deployed_on",
            "recovered_on",
            "metadata",
            "collection_metadata",
            "commentaries",
            "created_on",
            "created_by",
        )
