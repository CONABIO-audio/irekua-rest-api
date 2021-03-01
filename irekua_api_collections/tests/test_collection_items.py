import pytest
from rest_framework.test import APIClient

# pylint: disable=wildcard-import,unused-wildcard-import
from irekua_database.tests.fixtures.users import *
from irekua_items.tests.fixtures.item_types import *
from irekua_collections.tests.fixtures.data_collections import *
from irekua_collections.tests.fixtures.collection_items import *


@pytest.mark.django_db
def test_collection_item_view_permissions(
    superuser,
    curator,
    developer,
    manager_A,
    manager_B,
    administrator_A,
    administrator_B,
    collection_user_A,
    collection_user_B,
    restricted_user_A,
    restricted_user_B,
    external_user_A,
    closed_collection_A,
    collection_item_factory,
    restrictive_licence,
):
    item = collection_item_factory(
        collection=closed_collection_A,
        created_by=collection_user_A,
        licence=restrictive_licence,
    )

    path = f"/api/collections/v1/collection_items/{item.id}/"

    client = APIClient()
    assert client.get(path).status_code == 404

    client.force_authenticate(user=superuser)
    assert client.get(path).status_code == 200

    client.force_authenticate(user=manager_A)
    assert client.get(path).status_code == 200

    client.force_authenticate(user=manager_B)
    assert client.get(path).status_code == 404

    client.force_authenticate(user=administrator_A)
    assert client.get(path).status_code == 200

    client.force_authenticate(user=administrator_B)
    assert client.get(path).status_code == 404

    client.force_authenticate(user=collection_user_A)
    assert client.get(path).status_code == 200

    client.force_authenticate(user=collection_user_B)
    assert client.get(path).status_code == 404

    client.force_authenticate(user=restricted_user_A)
    assert client.get(path).status_code == 404

    client.force_authenticate(user=restricted_user_B)
    assert client.get(path).status_code == 404

    client.force_authenticate(user=external_user_A)
    assert client.get(path).status_code == 404
    client.logout()
