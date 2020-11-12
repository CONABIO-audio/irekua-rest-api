from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r"device_types", views.DeviceTypeViewSet)
router.register(r"devices", views.DeviceViewSet)
router.register(r"physical_devices", views.PhysicalDeviceViewSet)
