from irekua_models.models import Model
from irekua_api_core.views import IrekuaModelViewSet

from irekua_api_models import serializers
from irekua_models import filters


class ModelViewSet(IrekuaModelViewSet):
    queryset = Model.objects.all()

    serializer_class = serializers.ModelDetailSerializer

    serializer_action_classes = {"create": serializers.ModelCreateSerializer}

    filterset_class = filters.models.Filter

    search_fields = filters.models.search_fields

    ordering_fields = filters.models.ordering_fields
