from irekua_geo.models import SiteDescriptorType
from irekua_api_core.serializers import IrekuaModelSerializer


class SiteDescriptorTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = SiteDescriptorType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "created_on",
        )


class SiteDescriptorTypeDetailSerializer(IrekuaModelSerializer):
    class Meta(SiteDescriptorTypeSerializer.Meta):
        fields = (
            *SiteDescriptorTypeSerializer.Meta.fields,
            "metadata",
            "source",
            "modified_on",
        )
