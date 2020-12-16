from irekua_collections.models import Collection
from irekua_api_core.serializers import IrekuaUserModelSerializer


class CollectionSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Collection

        fields = (
            "id",
            "url",
            "name",
            "description",
            "created_on",
        )
