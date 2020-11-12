from irekua_geo.models import SiteType
from irekua_api_core.serializers import IrekuaModelSerializer
from .site_descriptor_types import SiteDescriptorTypeSerializer
from .site_descriptor_types import SiteDescriptorTypeDetailSerializer


class SiteTypeSerializer(IrekuaModelSerializer):
    site_descriptor_types = SiteDescriptorTypeSerializer(read_only=True, many=True)

    class Meta:
        model = SiteType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "site_descriptor_types",
            "point_site",
            "linestring_site",
            "multilinestring_site",
            "multipoint_site",
            "multipolygon_site",
            "polygon_site",
            "created_on",
        )


class SiteTypeDetailSerializer(IrekuaModelSerializer):
    site_descriptor_types = SiteDescriptorTypeDetailSerializer(
        read_only=True, many=True
    )

    class Meta(SiteTypeSerializer.Meta):
        fields = (
            *SiteTypeSerializer.Meta.fields,
            "metadata_schema",
            "site_descriptor_types",
            "modified_on",
        )
