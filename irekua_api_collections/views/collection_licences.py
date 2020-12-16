from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionLicence
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionLicenceViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = CollectionLicence.objects.all()

    serializer_class = serializers.CollectionLicenceSerializer

    filterset_class = filters.collection_licences.Filter

    search_fields = filters.collection_licences.search_fields

    ordering_fields = filters.collection_licences.ordering_fields
