from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r'item_types', views.ItemTypeViewSet)
router.register(r'licence_types', views.LicenceTypeViewSet)
router.register(r'licences', views.LicenceViewSet)
router.register(r'items', views.ItemViewSet)
