from rest_framework import serializers
from irekua_database.models import Role

from .base import IrekuaModelSerializer


class RoleSerializer(IrekuaModelSerializer):
    permissions = serializers.SlugRelatedField(
        slug_field='code_name',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Role
        fields = (
            'id',
            'name',
            'description',
            'icon',
            'permissions',
        )
