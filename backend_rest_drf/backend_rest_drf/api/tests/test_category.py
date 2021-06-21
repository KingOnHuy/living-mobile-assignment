from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from store.models import Store, Category
from store.serializers import StoreSerializer, CategorySerializer

import json


class CategoryTestCase(APITestCase):
    def setUp(self) -> None:
        self.root_path_v1 = '/v1/'
        User.objects.create_user(
            username='testUser',
            password='qwer1234',
        )
        User.objects.create_user(
            username='testUserAdmin',
            password='qwer1234',
            is_superuser=True,
        )
        storeInstance = Store.objects.create(
            name='Test set 00',
            description='test set',
            rating=1234,
        )
        self.storeTestData = StoreSerializer(storeInstance).data

        self.categoryTestData = CategorySerializer(
            Category.objects.create(
                name='Test set 00',
                storeId=storeInstance,
            )
        ).data
        Category.objects.create(
            name='Test set 01',
            storeId=storeInstance,
        )
        print('====== Run Test Category ======')
        return super().setUp()

    def test_category_admin_can_list(self):
        print('test_category_admin_can_list')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.get(
            self.root_path_v1 + 'category/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)

        self.assertEqual(reqContent['count'], 2)
        self.assertEqual(len(reqContent['results']), 2)

    def test_category_admin_can_create(self):
        print('test_category_admin_can_create')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'name': 'Test Create Category',
            'storeId': self.storeTestData['id'],
        }
        req = client.post(
            self.root_path_v1 + 'category/',
            expected_json,
        )
        self.assertEqual(req.status_code, 201)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent['name'], expected_json['name'])
        self.assertEqual(reqContent['storeId'],
                         expected_json['storeId'])

    def test_category_admin_can_get(self):
        print(f'test_category_admin_can_get {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'name': 'Test Create Category',
            'storeId': self.storeTestData['id'],
        }
        req = client.get(
            self.root_path_v1 + f'category/{self.storeTestData["id"]}/',
            expected_json,
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, self.storeTestData)

    def test_category_admin_can_get(self):
        print(f'test_category_admin_can_get {self.categoryTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        print(self.categoryTestData)
        req = client.get(
            self.root_path_v1 + f'category/{self.categoryTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, self.categoryTestData)

    def test_category_admin_can_update_all_PUT(self):
        print(
            f'test_category_admin_can_update_all_PUT {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.categoryTestData["id"],
            'storeId': self.storeTestData['id'],
            'name': 'Test Update All Category PUT',
        }
        req = client.put(
            self.root_path_v1 + f'category/{self.categoryTestData["id"]}/',
            expected_json,
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_category_admin_can_update_PATCH(self):
        print(
            f'test_category_admin_can_update_some_PATCH {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.categoryTestData['id'],
            'storeId': self.storeTestData['id'],
            'name': 'Test Edit Category PATCH',
        }
        req = client.patch(
            self.root_path_v1 + f'category/{self.categoryTestData["id"]}/',
            {
                'name': 'Test Edit Category PATCH',
            },
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_category_admin_can_update_delete_DELETE(self):
        print(
            f'test_category_admin_can_update_delete_DELETE {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.delete(
            self.root_path_v1 + f'category/{self.categoryTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 204)
