from irekua_collections.models import DeploymentType
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_collections import serializers
from irekua_collections import filters


class DeploymentTypeViewSet(IrekuaReadOnlyViewSet):
    queryset = DeploymentType.objects.all()

    serializer_class = serializers.DeploymentTypeSerializer

    serializer_action_classes = {"retrieve": serializers.DeploymentTypeDetailSerializer}

    filterset_class = filters.deployment_types.Filter

    search_fields = filters.deployment_types.search_fields

    ordering_fields = filters.deployment_types.ordering_fields
