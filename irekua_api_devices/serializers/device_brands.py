from irekua_devices.models import DeviceBrand
from irekua_api_core.serializers import IrekuaModelSerializer


class DeviceBrandSerializer(IrekuaModelSerializer):
    class Meta:
        model = DeviceBrand

        fields = (
            "name",
            "website",
            "logo",
        )
