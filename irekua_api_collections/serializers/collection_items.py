from irekua_collections.models import CollectionItem
from irekua_api_items.serializers import ItemSerializer


class CollectionItemSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        model = CollectionItem

        fields = (
            *ItemSerializer.Meta.fields,
            "collection",
            "sampling_event",
            "collection_device",
            "collection_site",
            "deployment",
            "collection_metadata",
        )
