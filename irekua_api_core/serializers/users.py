from irekua_database.models import User

from .base import IrekuaModelSerializer
from .institutions import InstitutionSerializer


class SimpleUserSerializer(IrekuaModelSerializer):
    class Meta:
        model = User

        fields = (
            "url",
            "id",
            "username",
        )


class UserSerializer(SimpleUserSerializer):
    class Meta(SimpleUserSerializer.Meta):
        fields = (
            *SimpleUserSerializer.Meta.fields,
            "first_name",
            "last_name",
            "email",
        )


class UserListSerializer(IrekuaModelSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
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
