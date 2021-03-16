# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from irekua_rest_api.serializers.base import IrekuaModelSerializer
from irekua_rest_api.serializers.base import IrekuaHyperlinkedModelSerializer

#  TODO: Remove annotation tool serializers and views from API when
# AnnotationTool model migration irekua-database -> selia-annotator is
# complete
# from selia_annotator.models import AnnotationTool
#
#
# class SelectSerializer(IrekuaModelSerializer):
#     class Meta:
#         model = AnnotationTool
#         fields = (
#             'url',
#             'name',
#         )
#
#
# class ListSerializer(IrekuaModelSerializer):
#     class Meta:
#         model = AnnotationTool
#         fields = (
#             'url',
#             'name',
#             'version',
#             'logo',
#         )
#
#
# class DetailSerializer(IrekuaHyperlinkedModelSerializer):
#     class Meta:
#         model = AnnotationTool
#         fields = (
#             'url',
#             'id',
#             'name',
#             'version',
#             'logo',
#             'website',
#             'created_on',
#             'modified_on'
#         )
#
#
# class CreateSerializer(IrekuaModelSerializer):
#     class Meta:
#         model = AnnotationTool
#         fields = (
#             'name',
#             'version',
#             'logo',
#             'website',
#         )
