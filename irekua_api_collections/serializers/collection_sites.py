from irekua_collections.models import CollectionSite
from irekua_api_core.serializers import IrekuaUserModelSerializer


class CollectionSiteSerializer(IrekuaUserModelSerializer):
    class Meta:
        model = CollectionSite

        fields = (
            "id",
            "url",
            "collection",
            "site",
            "collection_metadata",
            "collection_name",
            "site_type",
            "created_on",
            "created_by",
        )
