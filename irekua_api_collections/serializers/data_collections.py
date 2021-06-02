from irekua_collections.models import Collection
from irekua_api_core.serializers import IrekuaUserModelSerializer


class SimpleCollectionSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = Collection

        fields = (
            "id",
            "url",
            "name",
        )


class CollectionSerializer(SimpleCollectionSerializer):
    class Meta(SimpleCollectionSerializer.Meta):
        fields = (
            *SimpleCollectionSerializer.Meta.fields,
            "description",
            "institutions",
            "created_on",
        )
