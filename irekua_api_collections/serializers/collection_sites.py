from irekua_collections.models import CollectionSite
from irekua_api_core.serializers import IrekuaUserModelSerializer
from irekua_api_geo.serializers import SiteSerializer
from irekua_api_geo.serializers import SimpleSiteDescriptorSerializer
from irekua_api_geo.serializers import SimpleSiteTypeSerializer


class CollectionSiteSerializer(IrekuaUserModelSerializer):
    site = SiteSerializer(read_only=True)

    site_descriptors = SimpleSiteDescriptorSerializer(
        many=True,
        read_only=True,
    )
    site_type = SimpleSiteTypeSerializer(read_only=True)

    class Meta:
        model = CollectionSite

        fields = (
            "id",
            "url",
            "collection",
            "site",
            "site_descriptors",
            "collection_metadata",
            "collection_name",
            "site_type",
            "created_on",
            "created_by",
        )
