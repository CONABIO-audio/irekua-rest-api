from django_filters import rest_framework as filters

from irekua_terms.models import Term
from irekua_terms.models import TermType

from irekua_api_core.filters import IrekuaFilter
from irekua_api_core.autocomplete import get_autocomplete_widget



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
    term_type = filters.ModelChoiceFilter(
        queryset=TermType.objects.all(),
        widget=get_autocomplete_widget(model=TermType),
    )

    class Meta:
        model = Term
        fields = {
            'value': ['exact', 'icontains'],
            'term_type__name': ['exact', 'icontains'],
        }
