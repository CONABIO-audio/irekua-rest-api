from django.utils.functional import lazy
from irekua_database.autocomplete import get_autocomplete_widget


class Choice:
    def __init__(self, queryset):
        self.queryset = queryset

    def __iter__(self):
        for choice in self.queryset:
            yield choice


def _render_widget(name, widget, queryset):
    widget.choices = Choice(queryset=queryset)
    return widget.render(
        name=name,
        value=None,
    )


_render_widget = lazy(_render_widget, str)


def get_autocomplete_style(name, model):
    """
    Get the rest_framework field style to render a select2 autocomplete form.

    This form will allow the user to dynamically search and select an
    option from a model table or a custom autocomplete view.
    """
    widget = get_autocomplete_widget(model=model)

    return {
        "base_template": "autocomplete.html",
        "media": widget.media,
        "widget": _render_widget(name, widget, model.objects.all()),
    }
