from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class TestUser(APITestCase):
    """
        Тестирование создание пользователя
    """
    def setUp(self):
        self.user = User.objects.create(email='admin@test.com')
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """
        Тест на создание пользователя
        """

        data = {
            "email": "test@example.com",
            "password": 1234,
            "tg_chat_id": 3333
        }
        response = self.client.post(
            '/users/create/', data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {'id': response.json()['id'],
             "password": response.json()['password'],
             "email": "test@example.com", "city": None,
             "first_name": "", 'date_joined': response.json()['date_joined'],
             "groups": [],
             "image": None,
             "is_active": True,
             "is_staff": False,
             "is_superuser": False,
             "last_login": response.json()['last_login'],
             "last_name": "",
             "phone": None,
             "tg_chat_id": response.json()['tg_chat_id'],
             "user_permissions": []})

        self.assertTrue(User.objects.all().count() == 2)

    def test_update_user(self):
        """
        Тест на изменение пользователя
        """
        data = {
            "email": "test@example.com",
            "password": 1234,
            "tg_chat_id": 4444
        }
        response = self.client.put(
            f'/users/update/{self.user.id}/', data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('tg_chat_id'), 4444)
        self.assertEqual(
            response.json(),
            {'id': response.json()['id'],
             "password": response.json()['password'],
             "email": "test@example.com", "city": None,
             "first_name": "", 'date_joined': response.json()['date_joined'],
             "groups": [],
             "image": None,
             "is_active": response.json()['is_active'],
             "is_staff": False,
             "is_superuser": False,
             "last_login": response.json()['last_login'],
             "last_name": "",
             "phone": None,
             "tg_chat_id": response.json()['tg_chat_id'],
             "user_permissions": []})
