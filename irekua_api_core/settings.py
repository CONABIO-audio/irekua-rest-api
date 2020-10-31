from irekua_database.settings import *


IREKUA_API_CORE_APPS = (
    [
        'irekua_api_core',
        'rest_framework',
        'django_filters',
        'dal',
        'dal_select2',
    ] +
    IREKUA_DATABASE_APPS
)


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'irekua_api_core.pagination.StandardResultsSetPagination',
    # 'DEFAULT_METADATA_CLASS': 'irekua_api_core.metadata.CustomMetadata',
    # 'EXCEPTION_HANDLER': 'irekua_api_core.exception_handler.custom_exception_handler',
    # 'DEFAULT_SCHEMA_CLASS': 'irekua_api_core.schemas.CustomSchema'
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'PAGE_SIZE': 10,
}
