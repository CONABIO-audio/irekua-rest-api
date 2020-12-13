from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import DeploymentItem
from irekua_collections import filters
from irekua_api_collections import serializers


class DeploymentItemViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = DeploymentItem.objects.all()

    serializer_class = serializers.DeploymentItemSerializer

    # serializer_action_classes = {"retrieve": serializers.DeploymentItemSerializer}

    # filterset_class = filters.deployment_items.Filter
    #
    # search_fields = filters.deployment_items.search_fields
    #
    # ordering_fields = filters.deployment_items.ordering_fields

    def get_queryset(self):
        return DeploymentItem.objects.all()
