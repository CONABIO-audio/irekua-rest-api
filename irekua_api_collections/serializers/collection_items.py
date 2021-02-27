from rest_framework import serializers
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

    def validate(self, data):
        data = super().validate(data)
        item = CollectionItem(**data)
        item.clean()
        return data


class CollectionItemValidationSerializer(CollectionItemSerializer):
    serializer_related_field = serializers.PrimaryKeyRelatedField

    class Meta(CollectionItemSerializer.Meta):
        fields = [
            field
            for field in CollectionItemSerializer.Meta.fields
            if field not in ["item_file", "filesize", "hash", "created_by"]
        ] + ["mime_type"]

    def validate(self, data):
        data = super().validate(data)
        item = CollectionItem(**data)
        item.clean()
        return data

    def save(self, **kwargs):
        return
