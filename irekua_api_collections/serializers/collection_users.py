from rest_framework import serializers

from irekua_collections.models import CollectionUser
from irekua_api_core.serializers import UserSerializer
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_core.serializers import SimpleRoleSerializer
from irekua_api_collections.serializers.data_collections import (
    SimpleCollectionSerializer,
)


class SimpleCollectionUserSerializer(IrekuaModelSerializer):
    user = UserSerializer(read_only=True)

    role = SimpleRoleSerializer(read_only=True)

    class Meta:
        model = CollectionUser

        fields = (
            "id",
            "user", 
            "role"
        )
