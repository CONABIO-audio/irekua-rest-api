from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"annotation_types", views.AnnotationTypeViewSet)
router.register(r"event_types", views.EventTypeViewSet)
