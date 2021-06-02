from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionSite
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionSiteViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    queryset = (
        CollectionSite.objects.all()
        .prefetch_related(
            "site_descriptors__descriptor_type",
            "parent_site__site_type",
            "parent_site__parent_site__site_type",
        )
        .select_related(
            "collection",
            "site_type",
            "site",
            "site__linestringsite",
            "site__multilinestringsite",
            "site__multipointsite",
            "site__multipolygonsite",
            "site__pointsite",
            "site__polygonsite",
            "created_by",
        )
    )

    serializer_class = serializers.CollectionSiteSerializer

    filterset_class = filters.collection_sites.Filter

    search_fields = filters.collection_sites.search_fields

    ordering_fields = filters.collection_sites.ordering_fields
