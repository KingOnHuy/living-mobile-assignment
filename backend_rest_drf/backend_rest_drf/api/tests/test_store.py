from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from store.models import Store
from store.serializers import StoreSerializer

import json


class StoreTestCase(APITestCase):
    def setUp(self) -> None:
        self.root_path_v1 = '/v1/'
        print('====== Setup Test ======')
        print('Create testUser')
        User.objects.create_user(
            username='testUser',
            password='qwer1234',
        )
        print('Create testUserAdmin')
        User.objects.create_user(
            username='testUserAdmin',
            password='qwer1234',
            is_superuser=True,
        )

        print('Create Store set')
        self.storeTestData = StoreSerializer(Store.objects.create(
            name='Test set 00',
            description='test set',
            rating=1234,
        )).data
        Store.objects.create(
            name='Test set 01',
            description='test set',
            rating=5678,
        )
        print('====== Run Test ======')
        return super().setUp()

    def test_store_admin_can_list(self):
        print('test_store_admin_can_list')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.get(
            self.root_path_v1 + 'store/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)

        self.assertEqual(reqContent['count'], 2)
        self.assertEqual(len(reqContent['results']), 2)

    def test_store_admin_can_create(self):
        print('test_store_admin_can_create')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'name': 'Test Create Store',
            'description': 'test create store description',
            'rating': 10,
        }
        req = client.post(
            self.root_path_v1 + 'store/',
            expected_json,
        )
        self.assertEqual(req.status_code, 201)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent['name'], expected_json['name'])
        self.assertEqual(reqContent['description'],
                         expected_json['description'])
        self.assertEqual(reqContent['rating'], expected_json['rating'])

    def test_store_admin_can_get(self):
        print(f'test_store_admin_can_get {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'name': 'Test Create Store',
            'description': 'test create store description',
            'rating': 10,
        }
        req = client.get(
            self.root_path_v1 + f'store/{self.storeTestData["id"]}/',
            expected_json,
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, self.storeTestData)

    def test_store_admin_can_get(self):
        print(f'test_store_admin_can_get {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.get(
            self.root_path_v1 + f'store/{self.storeTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, self.storeTestData)

    def test_store_admin_can_update_all_PUT(self):
        print(
            f'test_store_admin_can_update_all_PUT {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.storeTestData["id"],
            'name': 'Test Create Store PUT',
            'description': 'test create store description PUT',
            'rating': 10,
        }
        req = client.put(
            self.root_path_v1 + f'store/{self.storeTestData["id"]}/',
            expected_json,
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_store_admin_can_update_all_PATCH(self):
        print(
            f'test_store_admin_can_update_some_PATCH {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.storeTestData["id"],
            'name': 'Test Create Store PATCH',
            'description': 'test set',
            'rating': 1234,
        }
        req = client.patch(
            self.root_path_v1 + f'store/{self.storeTestData["id"]}/',
            {
                'name': 'Test Create Store PATCH',
            },
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_store_admin_can_update_delete_DELETE(self):
        print(
            f'test_store_admin_can_update_delete_DELETE {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.delete(
            self.root_path_v1 + f'store/{self.storeTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 204)
