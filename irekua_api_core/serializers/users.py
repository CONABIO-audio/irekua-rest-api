from irekua_database.models import User

from .base import IrekuaModelSerializer


class UserSerializer(IrekuaModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_developer',
            'is_curator',
            'is_model',
        )
