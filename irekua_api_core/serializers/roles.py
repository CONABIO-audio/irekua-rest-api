from rest_framework import serializers
from irekua_database.models import Role

from .base import IrekuaModelSerializer


class SimpleRoleSerializer(IrekuaModelSerializer):

    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "description",
        )

class RoleSerializer(SimpleRoleSerializer):
    permissions = serializers.SlugRelatedField(
        slug_field="codename",
        many=True,
        read_only=True,
    )

    class Meta(SimpleRoleSerializer.Meta):
        fields = (
            *SimpleRoleSerializer.Meta.fields,
            "icon",
            "permissions",
        )
