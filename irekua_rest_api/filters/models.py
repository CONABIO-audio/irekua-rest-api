from irekua_models.models import Model
from .utils import BaseFilter


search_fields = (
    'name',
)


class Filter(BaseFilter):
    class Meta:
        model = Model
        fields = (
            'name',
        )
