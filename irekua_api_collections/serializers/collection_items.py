from rest_framework import serializers
from irekua_collections.models import CollectionItem

from irekua_api_items.serializers import ItemSerializer
from irekua_api_items.serializers import ItemUpdateSerializer


class CollectionItemSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        model = CollectionItem

        fields = (
            *ItemSerializer.Meta.fields,
            "collection",
            "collection_device",
            "collection_metadata",
            "collection_site",
            "deployment",
            "sampling_event",
        )

    def validate(self, data):
        data = super().validate(data)
        item = CollectionItem(**data)
        item.clean()
        return data

    def create(self, validated_data):
        item = CollectionItem(**validated_data)
        item.clean()
        item.save()
        return item


class CollectionItemUpdateSerializer(ItemUpdateSerializer):
    class Meta(ItemUpdateSerializer.Meta):
        model = CollectionItem

        fields = (
            *ItemUpdateSerializer.Meta.fields,
            "collection_metadata",
        )

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.clean()
        instance.save()
        return instance

    def validate(self, data):
        if getattr(self, "instance", None) is None:
            return

        data = super().validate(data)
        current_state = self.instance.__dict__.copy()

        try:
            self.instance.__dict__.update(data)
            self.instance.clean()

        except Exception as error:
            self.instance.__dict__.update(current_state)
            raise error

        finally:
            self.instance.__dict__.update(current_state)

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
