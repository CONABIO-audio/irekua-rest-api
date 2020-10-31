from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()
router.register(r'term_types', views.TermTypeViewSet)
router.register(r'terms', views.TermViewSet)
router.register(r'entailments', views.EntailmentViewSet)
