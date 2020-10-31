from irekua_terms.models import EntailmentType
from irekua_api_core.serializers import IrekuaModelSerializer


class EntailmentTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = EntailmentType

        fields = (
            'id',
        )
