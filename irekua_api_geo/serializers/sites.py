import json
from rest_framework import serializers

from irekua_geo.models import Site
from irekua_api_core.serializers import IrekuaModelSerializer


class SiteSerializer(IrekuaModelSerializer):
    geometry = serializers.SerializerMethodField("get_geometry")

    class Meta:
        model = Site

        fields = (
            "url",
            "id",
            "name",
            "locality",
            "geometry",
        )

    def get_geometry(self, obj):
        return json.loads(obj.geom().geojson)
