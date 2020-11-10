from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r'locality_types', views.LocalityTypeViewSet)
router.register(r'localities', views.LocalityViewSet)
router.register(r'site_descriptor_types', views.SiteDescriptorTypeViewSet)
router.register(r'site_descriptors', views.SiteDescriptorViewSet)
