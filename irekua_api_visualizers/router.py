from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"visualizers", views.VisualizersViewSet)
router.register(r"visualizer_versions", views.VisualizerVersionViewSet)
router.register(r"annotation_visualizers", views.AnnotationVisualizersViewSet)
router.register(r"visualizer_modules", views.VisualizerModuleViewSet)
