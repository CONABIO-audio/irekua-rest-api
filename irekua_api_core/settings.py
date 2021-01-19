from irekua_database.settings import *


IREKUA_API_CORE_APPS = [
    "irekua_api_core",
    "rest_framework",
    "django_filters",
    "crispy_forms",
    "dal",
    "dal_select2",
] + IREKUA_DATABASE_APPS


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "irekua_api_core.pagination.StandardResultsSetPagination",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "irekua_api_core.renderers.IrekuaAPIRenderer",
    ],
    "PAGE_SIZE": 10,
}
