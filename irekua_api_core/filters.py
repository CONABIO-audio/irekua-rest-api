from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
import django_filters


class IrekuaFilter(django_filters.FilterSet):
    created_on__lt = django_filters.DateTimeFilter(
        field_name='created_on',
        lookup_expr='lt',
        label=_('Created before than'),
        widget=forms.DateTimeInput)

    created_on__gt = django_filters.DateTimeFilter(
        field_name='created_on',
        lookup_expr='gt',
        label=_('Created after than'),
        widget=forms.DateTimeInput)

    modified_on__lt = django_filters.DateTimeFilter(
        field_name='modified_on',
        lookup_expr='lt',
        label=_('Modified before than'),
        widget=forms.DateTimeInput)

    modified_on__gt = django_filters.DateTimeFilter(
        field_name='modified_on',
        lookup_expr='gt',
        label=_('Modified after than'),
        widget=forms.DateTimeInput)


class IrekuaUserFilter(IrekuaFilter):
    created_by = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all()
    )
