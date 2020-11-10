from django.conf.urls import url, include
from .router import router


urlpatterns = [
    url('v1/', include((router.urls, 'irekua_api_items'), namespace='v1')),
    url('autocomplete/', include('irekua_api_items.autocomplete')),
]
