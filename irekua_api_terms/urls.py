from django.conf.urls import url, include
from .router import router


urlpatterns = [
    url('v1/', include(router.urls)),
    url('autocomplete/', include('irekua_api_terms.autocomplete')),
]
