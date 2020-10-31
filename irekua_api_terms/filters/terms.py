from irekua_terms.models import Term
from irekua_api_core.filters import IrekuaFilter



search_fields = (
    'term_type__name',
    'value',
    'description',
)


ordering_fields = (
    'created_on',
    'value',
    'term_type',
)


class Filter(IrekuaFilter):
    class Meta:
        model = Term
        fields = {
            'value': ['exact', 'icontains'],
            'term_type': ['exact'],
            'term_type__name': ['exact', 'icontains'],
        }
