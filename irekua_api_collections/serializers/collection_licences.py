from irekua_collections.models import CollectionLicence
from irekua_api_items.serializers import LicenceSerializer


class CollectionLicenceSerializer(LicenceSerializer):
    class Meta(LicenceSerializer.Meta):
        model = CollectionLicence

        fields = (
            *LicenceSerializer.Meta.fields,
            "collection",
            "collection_metadata",
        )
