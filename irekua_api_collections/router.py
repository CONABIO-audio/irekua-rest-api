from irekua_api_core.routers import IrekuaAPIRouter

from . import views


router = IrekuaAPIRouter()

router.register(
    r"deployment_types",
    views.DeploymentTypeViewSet,
)
router.register(
    r"sampling_event_types",
    views.SamplingEventTypeViewSet,
)
router.register(
    r"collection_items",
    views.CollectionItemViewSet,
    basename="collectionitem",
)
router.register(
    r"collection_sites",
    views.CollectionSiteViewSet,
)
router.register(
    r"collection_devices",
    views.CollectionDeviceViewSet,
)
router.register(
    r"collections",
    views.CollectionViewSet,
    basename="collection",
)
router.register(
    r"collection_licences",
    views.CollectionLicenceViewSet,
)
router.register(
    r"sampling_events",
    views.SamplingEventViewSet,
)
router.register(
    r"deployments",
    views.DeploymentViewSet,
)
router.register(
    r"collection_annotations",
    views.CollectionAnnotationViewSet,
)
