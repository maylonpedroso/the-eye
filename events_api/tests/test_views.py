from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase


class EventsViewSetTest(APITestCase):

    def test_events_creation(self):
        data = {
            "session_id": "s",
            "category": "a",
            "name": "n",
            "data": "{}",
            "timestamp": datetime.utcnow().isoformat()
        }

        response = self.client.post(
            reverse('events_api:events-list'), data=data
        )

        self.assertEqual(response.status_code, 201)
