from django.db import models
from django.contrib.admin.widgets import AutocompleteSelect
import django_filters

from irekua_terms.models import Entailment
from irekua_api_core.filters import IrekuaFilter


search_fields = (
    'source__value',
    'target__value',
    'source__term_type__name',
    'target__term_type__name',
)


ordering_fields = (
    'created_on',
)

class Filter(IrekuaFilter):
    class Meta:
        model = Entailment

        fields = {
            'source': ['exact'],
            'target': ['exact'],
            'source__term_type': ['exact'],
            'target__term_type': ['exact'],
            'source__value': ['exact', 'icontains'],
            'target__value': ['exact', 'icontains'],
            'source__term_type__name': ['exact', 'icontains'],
            'target__term_type__name': ['exact', 'icontains'],
        }
        # 
        # filter_overrides = {
        #      models.ForeignKey: {
        #          'filter_class': django_filters.ModelChoiceFilter,
        #          'extra': lambda f: {
        #              'widget': get_widget(f),
        #          },
        #      },
        #  }
