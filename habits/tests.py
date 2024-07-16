from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    """
    Тестирование создания, изменения и получения урока
    """
    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.habit = Habits.objects.create(owner=self.user, place="улица", time="20:00", action="test", duration=2)
        self.client.force_authenticate(user=self.user)

    def test_habits_create(self):
        url = reverse('habits:habits_create')
        data = {
            "owner": self.user.pk,
            "place": "test",
            "time": "10:00",
            "action": "test",
            "duration": 2,

        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get('place', 'time'), "test", "test_2")
        self.assertTrue(Habits.objects.all().count(), 2)

    def test_habits_update(self):
        url = reverse('habits:habits_update', args=(self.habit.pk,))
        data = {
            "owner": self.user.pk,
            "place": "test2",
            "time": "12:00",
            "action": "test",
            "duration": 2,

        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('place', 'time',), 'test2', '12:00')

    def test_habits_retrieve(self):
        url = reverse('habits:habits_detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('place', 'time'), 'улица', '12:00')

    def test_habit_delete(self):
        url = reverse('habits:habits_delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)

    def test_habits_list(self):
        url = reverse('habits:habits_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.habit.pk,
                               'place': self.habit.place,
                               'time': response.json()['results'][0]['time'],
                               'action': 'test',
                               'duration': self.habit.duration,
                               'is_daily': True,
                               'is_good': True,
                               'is_public': True,
                               'prize': None,
                               'owner': response.json()['results'][0]['owner'],
                               'related': None}]}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habits_public_list(self):
        url = reverse('habits:public_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'id': self.habit.pk,
                               'place': self.habit.place,
                               'time': response.json()['results'][0]['time'],
                               'action': 'test',
                               'duration': self.habit.duration,
                               'is_daily': True,
                               'is_good': True,
                               'is_public': True,
                               'prize': None,
                               'owner': response.json()['results'][0]['owner'],
                               'related': None}]}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
