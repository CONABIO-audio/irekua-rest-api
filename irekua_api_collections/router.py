from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"deployment_types", views.DeploymentTypeViewSet)
router.register(r"sampling_event_types", views.SamplingEventTypeViewSet)
router.register(r"deployment_items", views.DeploymentItemViewSet)
