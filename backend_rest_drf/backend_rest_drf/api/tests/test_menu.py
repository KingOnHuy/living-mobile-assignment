from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from store.models import Store, Category, Menu
from store.serializers import StoreSerializer, CategorySerializer, MenuSerializer

import json


class MenuTestCase(APITestCase):
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
            name='Test Store set 00',
            description='test set',
            rating=1234,
        )
        self.storeTestData = StoreSerializer(storeInstance).data

        categoryInstance = Category.objects.create(
            name='Test Category set 00',
            storeId=storeInstance,
        )
        self.categoryTestData = CategorySerializer(
            categoryInstance
        ).data
        Category.objects.create(
            name='Test Category set 01',
            storeId=storeInstance,
        )
        print('')

        self.menuTestData = MenuSerializer(
            Menu.objects.create(
                name='Test Menu set 00',
                categoryId=categoryInstance,
                price=9090,
            )
        ).data
        Menu.objects.create(
            name='Test Menu set 01',
            categoryId=categoryInstance,
                price=9191,
        )
        print('')
        print('====== Run Test Menu ======')
        return super().setUp()

    def test_menu_admin_can_list(self):
        print('test_menu_admin_can_list')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.get(
            self.root_path_v1 + 'menu/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)

        self.assertEqual(reqContent['count'], 2)
        self.assertEqual(len(reqContent['results']), 2)

    def test_menu_admin_can_create(self):
        print('test_menu_admin_can_create')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'name': 'Test Create Category',
            'categoryId': self.categoryTestData['id'],
            'price': 9292,
        }
        req = client.post(
            self.root_path_v1 + 'menu/',
            expected_json,
        )
        self.assertEqual(req.status_code, 201)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent['name'], expected_json['name'])
        self.assertEqual(reqContent['categoryId'],
                         expected_json['categoryId'])
        self.assertEqual(reqContent['price'],
                         expected_json['price'])

    def test_menu_admin_can_get(self):
        print(f'test_menu_admin_can_get {self.menuTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.menuTestData['id'],
            'name': self.menuTestData['name'],
            'categoryId': self.categoryTestData['id'],
            'price': self.menuTestData['price'],
        }
        req = client.get(
            self.root_path_v1 + f'menu/{self.menuTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_menu_admin_can_update_all_PUT(self):
        print(
            f'test_menu_admin_can_update_all_PUT {self.menuTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.menuTestData["id"],
            'categoryId': self.categoryTestData['id'],
            'name': 'Test Update All Category PUT',
            'price': 9494,
        }
        req = client.put(
            self.root_path_v1 + f'menu/{self.menuTestData["id"]}/',
            expected_json,
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_menu_admin_can_update_PATCH(self):
        print(
            f'test_menu_admin_can_update_some_PATCH {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        expected_json = {
            'id': self.menuTestData['id'],
            'categoryId': self.categoryTestData['id'],
            'name': 'Test Edit Category PATCH',
            'price': self.menuTestData['price'],
        }
        req = client.patch(
            self.root_path_v1 + f'menu/{self.menuTestData["id"]}/',
            {
                'name': 'Test Edit Category PATCH',
            },
        )
        self.assertEqual(req.status_code, 200)
        reqContent = json.loads(req.content)
        self.assertEqual(reqContent, expected_json)

    def test_menu_admin_can_update_delete_DELETE(self):
        print(
            f'test_menu_admin_can_update_delete_DELETE {self.storeTestData["id"]}')
        client = APIClient()
        client.login(username='testUserAdmin', password='qwer1234')
        req = client.delete(
            self.root_path_v1 + f'menu/{self.menuTestData["id"]}/',
        )
        self.assertEqual(req.status_code, 204)
