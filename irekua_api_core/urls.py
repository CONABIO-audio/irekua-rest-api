from django.conf.urls import url, include
from .routers import router


urlpatterns = [
    url("auth/", include("rest_framework.urls", namespace="rest_framework")),
    url("irekua/autocomplete/", include("irekua_api_core.autocomplete")),
    url("irekua/v1/", include(router.urls)),
]
