from irekua_database.models import User
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_core import serializers
from irekua_api_core.filters import users as filters


class UserViewSet(IrekuaReadOnlyViewSet):
    queryset = User.objects.all()

    serializer_class = serializers.UserListSerializer

    serializer_action_classes = {"retrieve": serializers.UserDetailSerializer}

    filterset_class = filters.Filter

    search_fields = filters.search_fields

    ordering_fields = filters.ordering_fields

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return User.objects.none()

        if user.is_special:
            return User.objects.all()

        return User.objects.filter(pk=user.pk)
