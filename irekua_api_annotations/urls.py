from django.conf.urls import url, include
from irekua_api_core.docs import generate_docs

from .router import router


urlpatterns = [
    url("v1/", include(router.urls)),
    url(
        "docs/",
        include(
            generate_docs(
                router,
                "irekua-annotations",
                title="Irekua Annotations API",
                description="REST API for irekua annotations models",
                version="1.0.0",
            )
        ),
    ),
]
