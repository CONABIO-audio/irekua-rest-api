from rest_framework import serializers

from irekua_collections.models import DeploymentItem
from irekua_api_core.serializers import UserSerializer
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_items.serializers import ItemSerializer

#
# from .item_types import ItemTypeSerializer
# from .licences import LicenceDetailSerializer


class DeploymentItemSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        model = DeploymentItem

        fields = (
            *ItemSerializer.Meta.fields,
            "deployment",
        )
