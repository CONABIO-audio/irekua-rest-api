from rest_framework import serializers

from irekua_database.models import User
from irekua_collections.models import CollectionSite
from irekua_api_core.serializers import IrekuaUserModelSerializer
from irekua_api_core.serializers import SimpleUserSerializer
from irekua_collections.models import CollectionUser
from irekua_api_geo.serializers import SimpleSiteSerializer
from irekua_api_geo.serializers import SimpleSiteDescriptorSerializer
from irekua_api_geo.serializers import SimpleSiteTypeSerializer
from irekua_api_collections.serializers.data_collections import (
    SimpleCollectionSerializer,
)

from .collection_users import SimpleCollectionUserSerializer

class SimpleCollectionSiteSerializer(IrekuaUserModelSerializer):
    site_type = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )

    parent_site = serializers.SerializerMethodField()

    class Meta:
        model = CollectionSite

        fields = (
            "id",
            "url",
            "collection_name",
            "site_type",
            "parent_site",
        )

    def get_parent_site(self, obj):
        if not obj.parent_site:
            return None

        serializer = SimpleCollectionSiteSerializer(
            obj.parent_site,
            context=self.context,
        )
        return serializer.data


class CollectionSiteSerializer(SimpleCollectionSiteSerializer):
    site = SimpleSiteSerializer(read_only=True)

    collection = SimpleCollectionSerializer(read_only=True)

    site_descriptors = SimpleSiteDescriptorSerializer(
        many=True,
        read_only=True,
    )

    site_type = SimpleSiteTypeSerializer(read_only=True)

    created_by = SimpleUserSerializer(read_only=True)

    class Meta(SimpleCollectionSiteSerializer.Meta):
        fields = (
            *SimpleCollectionSiteSerializer.Meta.fields,
            "collection",
            "site",
            "site_descriptors",
            "collection_metadata",
            "created_on",
            "created_by",
        )

class CollectionSiteDetailSerializer(SimpleCollectionSiteSerializer):
    site = SimpleSiteSerializer(read_only=True)

    collection = SimpleCollectionSerializer(read_only=True)

    site_descriptors = SimpleSiteDescriptorSerializer(
        many=True,
        read_only=True,
    )

    associated_users = serializers.SerializerMethodField()

    site_type = SimpleSiteTypeSerializer(read_only=True)

    created_by = SimpleUserSerializer(read_only=True)

    class Meta(SimpleCollectionSiteSerializer.Meta):
        fields = (
            *SimpleCollectionSiteSerializer.Meta.fields,
            "collection",
            "site",
            "site_descriptors",
            "collection_metadata",
            "associated_users",
            "created_on",
            "created_by",
        )

    def get_associated_users(self, obj):

        users = User.objects.filter(collectionsite=obj.id)

        queryset = CollectionUser.objects.filter(user_id__in=[user.id for user in users])
        
        serializer = SimpleCollectionUserSerializer(
            queryset, 
            many=True,
            context=self.context)

        return serializer.data
