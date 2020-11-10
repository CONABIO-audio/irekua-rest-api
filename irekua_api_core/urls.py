from django.conf.urls import url, include


urlpatterns = [
    url('auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('autocomplete/', include('irekua_api_core.autocomplete'))
]
