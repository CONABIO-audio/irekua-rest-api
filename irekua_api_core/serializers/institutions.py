from irekua_database.models import Institution

from .base import IrekuaModelSerializer


class InstitutionSerializer(IrekuaModelSerializer):
    class Meta:
        model = Institution
        fields = (
            "id",
            "institution_name",
            "institution_code",
            "country",
            "address",
            "website",
            "logo",
        )
