from irekua_devices.models import PhysicalDevice
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner
from irekua_api_core.permissions import IsAuthenticated
from irekua_api_core.views import IrekuaModelViewSet

from irekua_api_devices import serializers
from irekua_devices import filters


class PhysicalDeviceViewSet(IrekuaModelViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = PhysicalDevice.objects.all()

    serializer_class = serializers.PhysicalDeviceSerializer

    serializer_action_classes = {
        "retrieve": serializers.PhysicalDeviceDetailSerializer,
        "create": serializers.PhysicalDeviceCreateSerializer,
        "update": serializers.PhysicalDeviceCreateSerializer,
        "partial_update": serializers.PhysicalDeviceCreateSerializer,
    }

    permission_action_classes = {"create": [IsAuthenticated]}

    filterset_class = filters.physical_devices.Filter

    search_fields = filters.physical_devices.search_fields

    ordering_fields = filters.physical_devices.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return PhysicalDevice.objects.none()

        if user.is_special:
            return PhysicalDevice.objects.all()

        return PhysicalDevice.objects.filter(created_by=user)
