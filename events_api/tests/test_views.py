from django.urls import reverse
from rest_framework.test import APITestCase

from events_api.models import Event


class EventsViewSetTest(APITestCase):

    def test_events_creation_with_timestamp(self):
        data = {
            "session_id": "s",
            "category": "a",
            "name": "n",
            "data": "{}",
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        response = self.client.post(
            reverse('events_api:events-list'), data=data, format='json'
        )

        self.assertEqual(response.status_code, 202)
        self.assertIsNotNone(Event.objects.all().first())

    def test_events_creation_without_timestamp(self):
        data = {
            "session_id": "s",
            "category": "a",
            "name": "n",
            "data": "{}",
        }

        response = self.client.post(
            reverse('events_api:events-list'), data=data, format='json'
        )

        self.assertEqual(response.status_code, 202)
        self.assertIsNotNone(Event.objects.all().first())
