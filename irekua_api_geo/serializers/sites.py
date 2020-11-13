import json
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

from irekua_geo.models import Site
from irekua_geo.models import get_site_class
from irekua_geo.models import Locality
from irekua_api_core.autocomplete import get_autocomplete_style
from irekua_api_core.serializers import IrekuaModelSerializer
from irekua_api_core.serializers import IrekuaUserModelSerializer
from .localities import LocalitySerializer


class SiteSerializer(IrekuaModelSerializer):
    geometry = serializers.SerializerMethodField("get_geometry")
    locality = LocalitySerializer(read_only=True)

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
        try:
            return json.loads(obj.geom().geojson)
        except:
            return None


class SiteGeometryField(GeometryField):
    def get_attribute(self, instance):
        try:
            return instance.geom()
        except:
            return None


class SiteCreateSerializer(IrekuaUserModelSerializer):
    locality = serializers.PrimaryKeyRelatedField(
        queryset=Locality.objects.all(),
        style=get_autocomplete_style(name="locality", model=Locality),
        help_text=_("Locality in which the site is located."),
        required=False,
        read_only=False,
    )

    altitude = serializers.FloatField(
        required=False,
        help_text=_("Altitude of site. (Only valid if site geometry is Point)"),
    )

    geometry = SiteGeometryField(help_text=_("Site geometry"))

    class Meta:
        model = Site

        fields = ("name", "locality", "geometry", "altitude")

    def create(self, validated_data):
        # Get geometry type from posted geometry
        print(validated_data)
        geometry = validated_data.pop("geometry")
        geometry_type = geometry.geom_type
        validated_data["geometry_type"] = geometry_type

        # Create base site
        site = super().create(validated_data)

        # Create the corresponding site of the correct
        # geometry
        site_class = get_site_class(geometry_type)
        geom_site = site_class(
            site_ptr=site,
            geometry=geometry,
        )
        geom_site.__dict__.update(site.__dict__)
        geom_site.save()

        return site
