import json
import pytest
from rest_framework.test import APIClient

# pylint: disable=wildcard-import,unused-wildcard-import
from irekua_database.tests.fixtures.users import *
from irekua_items.tests.fixtures.item_types import *
from irekua_items.tests.fixtures.mime_types import *
from irekua_items.tests.fixtures.items import *
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


@pytest.mark.django_db
def test_collection_item_change_permissions(
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
    def permission_checker_factory(item):
        path = f"/api/collections/v1/collection_items/{item.id}/"

        def check_permission(user, expected_code):
            client = APIClient()

            if user is not None:
                client.force_authenticate(user=user)

            assert client.put(path, {"hash": "a"}).status_code == expected_code

            client.logout()

        return check_permission

    item1 = collection_item_factory(
        collection=closed_collection_A,
        created_by=collection_user_A,
        licence=restrictive_licence,
    )
    check_permission1 = permission_checker_factory(item1)

    check_permission1(None, 404)
    check_permission1(superuser, 200)
    check_permission1(curator, 200)
    check_permission1(developer, 403)
    check_permission1(manager_A, 200)
    check_permission1(manager_B, 404)
    check_permission1(administrator_A, 200)
    check_permission1(administrator_B, 404)
    check_permission1(collection_user_A, 200)
    check_permission1(collection_user_B, 404)
    check_permission1(restricted_user_A, 404)
    check_permission1(restricted_user_B, 404)
    check_permission1(external_user_A, 404)

    #  item2 = collection_item_factory(
    #      collection=closed_collection_A,
    #      created_by=restricted_user_A,
    #      licence=restrictive_licence,
    #  )
    #  assert item1.pk != item2.pk
    #  check_permission2 = permission_checker_factory(item2)

    #  check_permission2(None, 404)
    #  check_permission2(superuser, 200)
    #  check_permission2(curator, 200)
    #  check_permission2(developer, 403)
    #  check_permission2(manager_A, 200)
    #  check_permission2(manager_B, 404)
    #  check_permission2(administrator_A, 200)
    #  check_permission2(administrator_B, 404)
    #  check_permission2(collection_user_A, 200)
    #  check_permission2(collection_user_B, 404)
    #  check_permission2(restricted_user_A, 200)
    #  check_permission2(restricted_user_B, 404)
    #  check_permission2(external_user_A, 404)


@pytest.mark.django_db
def test_collection_item_create_permissions(
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
    item_type_A,
    restrictive_licence,
    audio_wav,
    collection_item_factory,
    generate_random_wav,
):
    path = "/api/collections/v1/collection_items/"

    def check_permission(user, expected_code):
        client = APIClient()

        if user is not None:
            client.force_authenticate(user=user)

        response = client.post(
            path,
            {
                "item_type": item_type_A.pk,
                "collection": closed_collection_A.pk,
                "item_file": generate_random_wav(),
                "media_info": json.dumps({}),
            },
        )

        assert response.status_code == expected_code
        client.logout()

    check_permission(None, 401)
    check_permission(superuser, 201)
    check_permission(curator, 403)
    check_permission(developer, 403)
    check_permission(manager_A, 201)
    check_permission(manager_B, 403)
    check_permission(administrator_A, 201)
    check_permission(administrator_B, 403)
    check_permission(collection_user_A, 201)
    check_permission(collection_user_B, 403)
    check_permission(restricted_user_A, 403)
    check_permission(restricted_user_B, 403)
    check_permission(external_user_A, 403)
