from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"models", views.ModelViewSet)
router.register(r"model_versions", views.ModelVersionViewSet)
router.register(r"model_runs", views.ModelRunViewSet)
router.register(r"model_predictions", views.ModelPredictionViewSet)
