from django.urls import path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


def generate_docs(router, app, title, description, version):
    return [
        path(
            "",
            TemplateView.as_view(
                template_name="irekua_api_core/swagger.html",
                extra_context={"schema_url": f"{app}-openapi-schema"},
            ),
            name=f"{app}-doc",
        ),
        path(
            r"schema/",
            get_schema_view(
                title=title,
                description=description,
                version=version,
                patterns=router.urls,
            ),
            name=f"{app}-openapi-schema",
        ),
    ]
