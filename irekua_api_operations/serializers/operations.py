from irekua_upload.models import Operation

from irekua_api_core.serializers import IrekuaModelSerializer


class OperationSerializer(IrekuaModelSerializer):
    class Meta:
        model = Operation

        fields = (
            'url',
            'id',
            'name',
            'description',
            'created_on',
        )


class OperationDetailSerializer(IrekuaModelSerializer):
    class Meta(OperationSerializer.Meta):
        fields = (
            *OperationSerializer.Meta.fields,
            'modified_on',
        )
