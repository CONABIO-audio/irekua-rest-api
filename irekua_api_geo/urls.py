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
                "irekua-geo",
                title="Irekua Geo API",
                description="REST API for irekua geo models",
                version="1.0.0",
            )
        ),
    ),
]
