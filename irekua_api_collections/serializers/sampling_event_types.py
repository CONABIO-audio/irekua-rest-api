from irekua_collections.models import SamplingEventType

from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_items.serializers import ItemTypeSerializer
from irekua_api_geo.serializers import SiteTypeSerializer
from irekua_api_geo.serializers import SiteTypeDetailSerializer
from irekua_api_schemas.serializers import SchemaSerializer
from .deployment_types import DeploymentTypeSerializer
from .deployment_types import DeploymentTypeDetailSerializer


class SamplingEventTypeSerializer(IrekuaModelSerializer):
    item_types = ItemTypeSerializer(many=True, read_only=True)

    site_types = SiteTypeSerializer(many=True, read_only=True)

    deployment_types = DeploymentTypeSerializer(many=True, read_only=True)

    class Meta:
        model = SamplingEventType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "restrict_deployment_types",
            "deployment_types",
            "restrict_item_types",
            "item_types",
            "restrict_site_types",
            "site_types",
            "restrict_deployment_positions",
            "deployment_distance",
        )


class SamplingEventTypeDetailSerializer(IrekuaModelSerializer):
    item_types = ItemTypeSerializer(many=True, read_only=True)

    site_types = SiteTypeDetailSerializer(many=True, read_only=True)

    deployment_types = DeploymentTypeDetailSerializer(many=True, read_only=True)

    metadata_schema = SchemaSerializer(read_only=True)

    class Meta(SamplingEventTypeSerializer.Meta):
        fields = (
            *SamplingEventTypeSerializer.Meta.fields,
            "metadata_schema",
            "created_on",
            "modified_on",
        )
