from irekua_database.models import User

from .base import IrekuaModelSerializer
from .institutions import InstitutionSerializer


class UserSerializer(IrekuaModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class UserListSerializer(IrekuaModelSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            "url",
            "id",
            *UserSerializer.Meta.fields,
            "is_developer",
            "is_curator",
            "is_model",
        )


class UserDetailSerializer(IrekuaModelSerializer):
    institutions = InstitutionSerializer(many=True, read_only=True)

    class Meta(UserListSerializer.Meta):
        fields = (
            *UserListSerializer.Meta.fields,
            "institutions",
        )
