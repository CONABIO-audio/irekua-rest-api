from irekua_dev_settings.settings import *
from irekua_database.settings import *
from irekua_rest_framework.settings import *

INSTALLED_APPS = (
    IREKUA_REST_API_APPS +
    IREKUA_DATABASE_APPS +
    IREKUA_BASE_APPS
)
