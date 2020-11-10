from rest_framework import serializers

from irekua_terms.models import Term
from irekua_api_core.serializers import IrekuaModelSerializer
from .term_types import TermTypeSerializer


class TermSerializer(IrekuaModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='term-detail')

    class Meta:
        model = Term

        fields = (
            'url',
            'id',
            'term_type',
            'value',
            'description',
            'created_on',
        )


class TermDetailSerializer(IrekuaModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='term-detail')
    term_type = TermTypeSerializer(read_only=True)

    class Meta(TermSerializer.Meta):
        fields = (
            *TermSerializer.Meta.fields,
            'metadata',
            'scope',
            'modified_on',
        )


class TermComplexSerializer(IrekuaModelSerializer):
    entailments = TermSerializer(
        read_only=True,
        many=True,
    )

    synonyms = TermSerializer(
        read_only=True,
        many=True,
    )

    url = serializers.HyperlinkedIdentityField(
        view_name='term-detail',
    )

    term_type = TermTypeSerializer(
        read_only=True,
    )

    class Meta(TermDetailSerializer.Meta):
        fields = (
            *TermDetailSerializer.Meta.fields,
            'entailments',
            'synonyms',
        )