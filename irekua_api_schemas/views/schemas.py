from irekua_schemas.models import Schema
from irekua_api_core.views import IrekuaReadOnlyViewSet

from irekua_api_schemas import serializers


class SchemaViewSet(IrekuaReadOnlyViewSet):
    queryset = Schema.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.SchemaDetailSerializer
    }

    serializer_class = serializers.SchemaSerializer
