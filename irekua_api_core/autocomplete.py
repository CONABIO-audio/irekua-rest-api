import re
from django.urls import path
from dal import autocomplete

from irekua_database.models import User


model_store = {}


def get_name_from_model(model):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', model.__name__).lower() + 's'


def register_autocomplete(model, urlpatterns, name=None):
    if name is None:
        name = get_name_from_model(model)

    url = f'{name}_autocomplete'

    def wrapper(ViewClass):
        urlpatterns.append(
            path(f'{name}/', ViewClass.as_view(), name=url)
        )

        return ViewClass

    return wrapper



class UsersAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()

        if self.q:
            qs = qs.filter(value__istartswith=self.q)

        return qs



urlpatterns = [
    path('users/', UsersAutocomplete.as_view(), name='users_autocomplete')
]
