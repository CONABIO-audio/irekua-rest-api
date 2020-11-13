from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"annotation_types", views.AnnotationTypeViewSet)
router.register(r"event_types", views.EventTypeViewSet)
router.register(r"annotations", views.AnnotationViewSet)
router.register(r"user_annotations", views.UserAnnotationViewSet)
