from rest_framework import serializers

from irekua_geo.models import SiteDescriptor
from irekua_api_core.serializers import IrekuaModelSerializer

from .site_descriptor_types import SiteDescriptorTypeSerializer
from .site_descriptor_types import SiteDescriptorTypeDetailSerializer


class SimpleSiteDescriptorSerializer(IrekuaModelSerializer):
    descriptor_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = SiteDescriptor

        fields = (
            "url",
            "id",
            "value",
            "descriptor_type",
        )


class SiteDescriptorSerializer(IrekuaModelSerializer):
    descriptor_type = SiteDescriptorTypeSerializer(read_only=True)

    class Meta:
        model = SiteDescriptor

        fields = (
            "url",
            "id",
            "value",
            "description",
            "descriptor_type",
            "created_on",
        )


class SiteDescriptorDetailSerializer(IrekuaModelSerializer):
    site_descriptor_type = SiteDescriptorTypeDetailSerializer(read_only=True)

    class Meta(SiteDescriptorSerializer.Meta):
        fields = (
            *SiteDescriptorSerializer.Meta.fields,
            "metadata",
            "modified_on",
        )
