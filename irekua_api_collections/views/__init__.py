from .collection_devices import CollectionDeviceViewSet
from .collection_annotations import CollectionAnnotationViewSet
from .collection_items import CollectionItemViewSet
from .collection_licences import CollectionLicenceViewSet
from .collection_sites import CollectionSiteViewSet
from .data_collections import CollectionViewSet
from .deployment_types import DeploymentTypeViewSet
from .sampling_event_types import SamplingEventTypeViewSet
from .sampling_events import SamplingEventViewSet
from .deployments import DeploymentViewSet


__all__ = [
    "CollectionDeviceViewSet",
    "CollectionAnnotationViewSet",
    "CollectionItemViewSet",
    "CollectionLicenceViewSet",
    "CollectionSiteViewSet",
    "CollectionViewSet",
    "DeploymentTypeViewSet",
    "SamplingEventTypeViewSet",
    "SamplingEventViewSet",
    "DeploymentViewSet",
]
