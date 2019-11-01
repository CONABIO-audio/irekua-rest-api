# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from irekua_database.models import Synonym

from . import terms


class SelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = (
            'url',
            'id',
        )


class ListSerializer(serializers.ModelSerializer):
    source_type = serializers.CharField(
        read_only=True,
        source='source.term_type.name')
    source_value = serializers.CharField(
        read_only=True,
        source='source.value')
    target_type = serializers.CharField(
        read_only=True,
        source='target.term_type.name')
    target_value = serializers.CharField(
        read_only=True,
        source='target.value')

    class Meta:
        model = Synonym
        fields = (
            'url',
            'id',
            'source_type',
            'source_value',
            'target_type',
            'target_value',
        )


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    source = terms.SelectSerializer(many=False, read_only=True)
    target = terms.SelectSerializer(many=False, read_only=True)

    class Meta:
        model = Synonym
        fields = (
            'url',
            'metadata',
            'source',
            'target',
            'created_on',
            'modified_on',
        )


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = (
            'source',
            'target',
            'metadata',
        )



class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = (
            'metadata',
        )
