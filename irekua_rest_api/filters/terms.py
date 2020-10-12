from irekua_terms.models import Term
from .utils import BaseFilter


search_fields = (
    'value',
)


class Filter(BaseFilter):
    class Meta:
        model = Term
        fields = (
            'value',
        )
