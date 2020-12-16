from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(
        "autocomplete/irekua/",
        include("irekua_database.autocomplete"),
    ),
    url(
        "autocomplete/schemas/",
        include("irekua_schemas.autocomplete"),
    ),
    url(
        "autocomplete/terms/",
        include("irekua_terms.autocomplete"),
    ),
    url(
        "autocomplete/items/",
        include("irekua_items.autocomplete"),
    ),
    url(
        "autocomplete/geo/",
        include("irekua_geo.autocomplete"),
    ),
    url(
        "autocomplete/devices/",
        include("irekua_devices.autocomplete"),
    ),
    url(
        "autocomplete/annotations/",
        include("irekua_annotations.autocomplete"),
    ),
    url(
        "autocomplete/collections/",
        include("irekua_collections.autocomplete"),
    ),
    url(
        "autocomplete/models/",
        include("irekua_models.autocomplete"),
    ),
    url(
        "api/",
        include("irekua_api_core.urls"),
    ),
    url(
        "api/schemas/",
        include("irekua_api_schemas.urls"),
    ),
    url(
        "api/terms/",
        include("irekua_api_terms.urls"),
    ),
    url(
        "api/operations/",
        include("irekua_api_operations.urls"),
    ),
    url(
        "api/items/",
        include("irekua_api_items.urls"),
    ),
    url(
        "api/geo/",
        include("irekua_api_geo.urls"),
    ),
    url(
        "api/devices/",
        include("irekua_api_devices.urls"),
    ),
    url(
        "api/annotations/",
        include("irekua_api_annotations.urls"),
    ),
    url(
        "api/collections/",
        include("irekua_api_collections.urls"),
    ),
    url(
        "api/models/",
        include("irekua_api_models.urls"),
    ),
    url(r"^admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
