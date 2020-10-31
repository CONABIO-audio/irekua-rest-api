from django.conf.urls import url, include
from .router import router


urlpatterns = [
    url('v1/', include(router.urls)),
    # url('docs/', include_docs_urls(title='Irekua REST API documentation')),
]
