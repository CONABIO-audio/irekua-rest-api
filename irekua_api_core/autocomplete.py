import re

from django.urls import path
from django.urls import reverse
from django.utils.functional import lazy
from dal import autocomplete

from irekua_database.models import User
from .widgets import SelectMultiple
from .widgets import Select


model_store = {}


def get_name_from_model(model):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', model.__name__).lower() + 's'


def get_viewname_from_model(model):
    return f'{get_name_from_model(model)}_autocomplete'


def register_autocomplete(model, urlpatterns, view_name=None):
    if view_name is None:
        view_name = get_viewname_from_model(model)

    model_store[model] = view_name

    def wrapper(ViewClass):
        urlpatterns.append(
            path(
                f'{get_name_from_model(model)}/',
                ViewClass.as_view(),
                name=view_name,
            )
        )

        return ViewClass

    return wrapper


lazy_reverse = lazy(reverse, str)


def get_autocomplete_widget(
        model=None,
        view_name=None,
        multiple=False,
        attrs=None,
        query=None):
    if view_name is None:
        view_name = model_store.get(model, get_viewname_from_model(model))

    if attrs is None:
        attrs = {'style': 'width: 100%;'}

    if multiple:
        return SelectMultiple(url=view_name, query=query, attrs=attrs)

    return Select(url=view_name, query=query, attrs=attrs)


urlpatterns = []


@register_autocomplete(User, urlpatterns)
class UsersAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()

        if self.q:
            qs = qs.filter(value__istartswith=self.q)

        return qs
