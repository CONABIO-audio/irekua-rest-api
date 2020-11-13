from rest_framework import routers

from . import views


class IrekuaAPIRouter(routers.DefaultRouter):
    pass


router = IrekuaAPIRouter()
router.register(r"users", views.UserViewSet)
router.register(r"institutions", views.InstitutionViewSet)
