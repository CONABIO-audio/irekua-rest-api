from django.conf.urls import url, include
from .router import router
from irekua_api_core.docs import generate_docs


urlpatterns = [
    url("v1/", include(router.urls)),
    url(
        "docs/",
        include(
            generate_docs(
                router,
                "irekua-devices",
                title="Irekua Devices API",
                description="REST API for irekua devices models",
                version="1.0.0",
            )
        ),
    ),
]
