# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from irekua_rest_api.serializers.base import IrekuaModelSerializer
from irekua_rest_api.serializers.base import IrekuaHyperlinkedModelSerializer
from irekua_database.models import AnnotationTool


class SelectSerializer(IrekuaModelSerializer):
    class Meta:
        model = AnnotationTool
        fields = (
            'url',
            'name',
        )


class ListSerializer(IrekuaModelSerializer):
    class Meta:
        model = AnnotationTool
        fields = (
            'url',
            'name',
            'version',
            'description',
            'logo',
        )


class DetailSerializer(IrekuaHyperlinkedModelSerializer):
    class Meta:
        model = AnnotationTool
        fields = (
            'url',
            'id',
            'name',
            'version',
            'description',
            'logo',
            'website',
            'configuration_schema',
            'created_on',
            'modified_on'
        )


class CreateSerializer(IrekuaModelSerializer):
    class Meta:
        model = AnnotationTool
        fields = (
            'name',
            'version',
            'description',
            'logo',
            'website',
            'configuration_schema',
        )
