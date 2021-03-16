from irekua_items.models import LicenceType
from irekua_api_core.serializers import IrekuaModelSerializer


class LicenceTypeSerializer(IrekuaModelSerializer):
    class Meta:
        model = LicenceType

        fields = (
            "url",
            "id",
            "name",
            "description",
            "icon",
            "document_template",
            "years_valid_for",
            "can_view",
            "can_download",
            "can_view_annotations",
            "can_annotate",
            "can_vote_annotations",
        )
