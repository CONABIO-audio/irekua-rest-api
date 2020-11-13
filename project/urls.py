from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url("api/", include("irekua_api_core.urls")),
    url("api/schemas/", include("irekua_api_schemas.urls")),
    url("api/terms/", include("irekua_api_terms.urls")),
    url("api/operations/", include("irekua_api_operations.urls")),
    url("api/items/", include("irekua_api_items.urls")),
    url("api/geo/", include("irekua_api_geo.urls")),
    url("api/devices/", include("irekua_api_devices.urls")),
    url("api/annotations/", include("irekua_api_annotations.urls")),
    url("api/collections/", include("irekua_api_collections.urls")),
    url(r"^admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
