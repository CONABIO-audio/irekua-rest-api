from rest_framework import serializers
from irekua_database.models import Role

from .base import IrekuaModelSerializer


class RoleSerializer(IrekuaModelSerializer):
    permissions = serializers.SlugRelatedField(
        slug_field="codename",
        many=True,
        read_only=True,
    )

    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "description",
            "icon",
            "permissions",
        )
