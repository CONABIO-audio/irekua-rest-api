from irekua_items.models import Licence
from irekua_api_core.serializers import UserSerializer
from irekua_api_core.serializers import IrekuaModelSerializer

from .licence_types import LicenceTypeSerializer


class LicenceSerializer(IrekuaModelSerializer):
    class Meta:
        model = Licence

        fields = (
            "url",
            "id",
            "licence_type",
            "document",
            "created_on",
            "created_by",
        )


class LicenceDetailSerializer(IrekuaModelSerializer):
    licence_type = LicenceTypeSerializer(read_only=True)

    created_by = UserSerializer(read_only=True)

    class Meta(LicenceSerializer.Meta):
        pass
