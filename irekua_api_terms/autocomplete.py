from django.urls import path
from django.db.models import Q
from dal import autocomplete

from irekua_terms.models import Term
from irekua_terms.models import TermType
from irekua_terms.models import EntailmentType
from irekua_terms.models import EntailmentType


class TermsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Term.objects.all()

        if self.q:
            qs = qs.filter(value__istartswith=self.q)

        return qs



urlpatterns = [
    path('terms/', TermsAutocomplete.as_view(), name='terms_autocomplete')
]
