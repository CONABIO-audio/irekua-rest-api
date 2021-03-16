from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"operations", views.OperationViewSet)
