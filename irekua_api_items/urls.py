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
                "irekua-items",
                title="Irekua Items API",
                description="REST API for irekua items models",
                version="1.0.0",
            )
        ),
    ),
]
