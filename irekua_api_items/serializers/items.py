from rest_framework import serializers

from irekua_items.models import Item
from irekua_api_core.serializers import UserSerializer
from irekua_api_core.serializers import IrekuaModelSerializer

from .item_types import ItemTypeSerializer
from .licences import LicenceDetailSerializer


class ItemUpdateSerializer(IrekuaModelSerializer):
    class Meta:
        model = Item

        fields = (
            "captured_on",
            "captured_on_day",
            "captured_on_hour",
            "captured_on_minute",
            "captured_on_month",
            "captured_on_second",
            "captured_on_timezone",
            "captured_on_year",
            "licence",
            "media_info",
            "metadata",
        )


class ItemSerializer(IrekuaModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    class Meta:
        model = Item

        fields = (
            "url",
            "id",
            "captured_on",
            "captured_on_day",
            "captured_on_hour",
            "captured_on_minute",
            "captured_on_month",
            "captured_on_second",
            "captured_on_timezone",
            "captured_on_year",
            "created_by",
            "created_on",
            "filesize",
            "hash",
            "item_file",
            "item_type",
            "licence",
            "media_info",
            "metadata",
            "tags",
        )


class ItemDetailSerializer(ItemSerializer):
    item_type = ItemTypeSerializer(read_only=True)

    licence = LicenceDetailSerializer(read_only=True)

    created_by = UserSerializer(read_only=True)

    class Meta(ItemSerializer.Meta):
        fields = (*ItemSerializer.Meta.fields,)
