from django.template import loader
from django.db.models.manager import Manager
from irekua_database.autocomplete import get_autocomplete_widget
from rest_framework.relations import ManyRelatedField, RelatedField
from rest_framework.renderers import BrowsableAPIRenderer, HTMLFormRenderer
from rest_framework.utils.field_mapping import ClassLookupDict


class Choice:
    def __init__(self, queryset):
        self.queryset = queryset

    def __iter__(self):
        for choice in self.queryset:
            yield choice


class IrekuaFormRenderer(HTMLFormRenderer):
    default_style = ClassLookupDict(
        {
            **HTMLFormRenderer.default_style.mapping,
            RelatedField: {
                "template": "irekua_api_core/custom_select.html",
            },
            ManyRelatedField: {
                "template": "irekua_api_core/custom_select.html",
            },
        }
    )

    def render_field(self, field, parent_style):
        if not isinstance(field._field, (RelatedField, ManyRelatedField)):
            return super().render_field(field, parent_style)

        style = self.default_style[field].copy()
        style.update(field.style)
        if "template_pack" not in style:
            style["template_pack"] = parent_style.get(
                "template_pack", self.template_pack
            )
        style["renderer"] = self

        if "template" in style:
            template_name = style["template"]
        else:
            template_name = (
                style["template_pack"].strip("/") + "/" + style["base_template"]
            )

        if isinstance(field._field, ManyRelatedField):
            queryset = field._field.child_relation.queryset
            model = queryset.model
            multiple = True
        else:
            queryset = field._field.queryset
            model = queryset.model
            multiple = False

        if isinstance(queryset, Manager):
            queryset = queryset.all()

        widget = get_autocomplete_widget(model=model, multiple=multiple)
        widget.choices = Choice(queryset=queryset)

        template = loader.get_template(template_name)
        context = {
            "field": field,
            "style": style,
            "widget": widget.render(field._field.field_name, None),
        }
        return template.render(context)


class IrekuaAPIRenderer(BrowsableAPIRenderer):
    form_renderer_class = IrekuaFormRenderer
