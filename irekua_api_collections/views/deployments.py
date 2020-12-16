from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import Deployment
from irekua_collections import filters
from irekua_api_collections import serializers


class DeploymentViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = Deployment.objects.all()

    serializer_class = serializers.DeploymentSerializer

    filterset_class = filters.deployments.Filter

    search_fields = filters.deployments.search_fields

    ordering_fields = filters.deployments.ordering_fields
