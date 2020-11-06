import os
from collections import OrderedDict

from irekua_dev_settings.settings import *
from irekua_api_core.settings import *
from irekua_api_schemas.settings import *
from irekua_api_terms.settings import *
from irekua_api_items.settings import *
from irekua_api_operations.settings import *


MIGRATE = False


MIGRATION_MODULES = {
    'irekua_database': None,
    'irekua_schemas': None,
    'irekua_items': None,
    'irekua_terms': None,
    'irekua_upload': None,
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]


INSTALLED_APPS = list(OrderedDict.fromkeys(
    IREKUA_BASE_APPS +
    IREKUA_API_CORE_APPS +
    IREKUA_API_SCHEMAS_APPS +
    IREKUA_API_TERMS_APPS +
    IREKUA_API_ITEMS_APPS +
    IREKUA_API_OPERATIONS_APPS
))
