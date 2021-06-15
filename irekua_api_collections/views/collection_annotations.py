from irekua_api_core.views import IrekuaModelViewSet
from irekua_api_core.permissions import IsAuthenticated

from irekua_collections.models import CollectionAnnotation
from irekua_collections import filters
from irekua_api_collections import serializers
from irekua_api_collections.permissions import CanViewAnnotation
from irekua_api_collections.permissions import CanCreateAnnotation
from irekua_api_collections.permissions import CanUpdateAnnotation
from irekua_api_collections.permissions import CanDeleteAnnotation

#  from irekua_api_collections.permissions import CanVoteAnnotation


class CollectionAnnotationViewSet(IrekuaModelViewSet):
    queryset = CollectionAnnotation.objects.all()

    serializer_class = serializers.CollectionAnnotationSerializer

    serializer_action_classes = {
        "retrieve": serializers.CollectionAnnotationDetailSerializer
    }

    filterset_class = filters.collection_annotations.Filter
    search_fields = filters.collection_annotations.search_fields
    ordering_fields = filters.collection_annotations.ordering_fields

    permission_action_classes = {
        "list": [IsAuthenticated],
        "create": [CanCreateAnnotation],
        "retrieve": [CanViewAnnotation],
        "update": [CanUpdateAnnotation],
        "partial_update": [CanUpdateAnnotation],
        "destroy": [CanDeleteAnnotation],
        # TODO: Vote endpoint
        #  "vote": [CanVoteAnnotation],
    }

    def get_queryset(self):
        return CollectionAnnotation.objects.can_view(self.request.user)
