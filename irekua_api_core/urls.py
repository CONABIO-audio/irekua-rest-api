from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework.authtoken import views

from .routers import router
from irekua_api_core.docs import generate_docs


urlpatterns = [
    url("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/token/", views.obtain_auth_token),
    url("irekua/v1/", include(router.urls)),
    url(
        "^docs/",
        include(
            generate_docs(
                router,
                "irekua-database",
                title="Irekua Database API",
                description="REST API for irekua database models",
                version="1.0.0",
            )
        ),
    ),
]
