import os
from collections import OrderedDict

from irekua_dev_settings.settings import *
from irekua_api_core.settings import *
from irekua_api_schemas.settings import *
from irekua_api_terms.settings import *
from irekua_api_items.settings import *
from irekua_api_operations.settings import *
from irekua_api_geo.settings import *
from irekua_api_devices.settings import *
from irekua_api_annotations.settings import *
from irekua_api_collections.settings import *


from irekua_types.settings import *
from irekua_models.settings import *
from irekua_organisms.settings import *
from irekua_annotators.settings import *
from irekua_visualizers.settings import *
from irekua_thumbnails.settings import *

MIGRATE = False


MIGRATION_MODULES = {
    "irekua_database": None,
    "irekua_schemas": None,
    "irekua_items": None,
    "irekua_terms": None,
    "irekua_upload": None,
    "irekua_geo": None,
    "irekua_models": None,
    "irekua_devices": None,
    "irekua_organisms": None,
    "irekua_annotators": None,
    "irekua_visualizers": None,
    "irekua_collections": None,
    "irekua_annotations": None,
    "irekua_thumbnails": None,
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]


INSTALLED_APPS = list(
    OrderedDict.fromkeys(
        IREKUA_BASE_APPS
        + IREKUA_API_CORE_APPS
        + IREKUA_API_SCHEMAS_APPS
        + IREKUA_API_TERMS_APPS
        + IREKUA_API_OPERATIONS_APPS
        + IREKUA_API_ITEMS_APPS
        + IREKUA_API_DEVICES_APPS
        + IREKUA_API_GEO_APPS
        + IREKUA_API_ANNOTATIONS_APPS
        + IREKUA_API_COLLECTIONS_APPS
        + IREKUA_ORGANISMS_APPS
        + IREKUA_MODELS_APPS
        + IREKUA_ANNOTATORS_APPS
        + IREKUA_VISUALIZERS_APPS
        + IREKUA_THUMBNAILS_APPS
    )
)
