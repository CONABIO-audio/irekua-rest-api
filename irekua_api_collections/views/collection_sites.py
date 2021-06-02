from django.db.models import Q
from rest_framework.permissions import AllowAny

from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_core.permissions import IsSpecial
from irekua_api_core.permissions import IsOwner

from irekua_collections.models import CollectionSite
from irekua_collections import filters
from irekua_api_collections import serializers


class CollectionSiteViewSet(IrekuaReadOnlyViewSet):
    permission_classes = [IsSpecial | IsOwner]

    permission_action_classes = {
        "list": [AllowAny],
    }

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

    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user

        is_open = Q(collection__is_open=True)
        if not user.is_authenticated:
            return queryset.filter(is_open)

        if user.is_special:
            return queryset

        is_manager = Q(collection__collection_type__admin=user)
        is_admin = Q(collection__administrators=user)
        is_user = Q(collection__users=user)
        is_own = Q(created_by=user)

        return queryset.filter(is_open | is_manager | is_admin | is_user | is_own)
