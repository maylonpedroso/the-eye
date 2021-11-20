from time import time
from unittest.mock import patch

from django.urls import reverse
from rest_framework.test import APITestCase

from authz.tokens import ClientTokenBackend
from events_api.models import Event

TOKEN_PAYLOAD = {
    "jti": "123456789",
    "sub": "client",
    "gty": "client-credentials",
    "iat": time(),
    "exp": time() + 3600,
}


class EventsViewSetTest(APITestCase):

    def test_events_creation_unauthorized_request(self):
        response = self.client.post(
            reverse('events_api:events-list'), data={}, format='json'
        )

        self.assertEqual(response.status_code, 401)
        self.assertIsNone(Event.objects.all().first())

    @patch.object(ClientTokenBackend, 'decode')
    def test_events_creation_with_timestamp(self, mock_decode):
        mock_decode.return_value = TOKEN_PAYLOAD
        data = {
            "session_id": "s",
            "category": "a",
            "name": "n",
            "data": "{}",
            "timestamp": "2021-01-01 09:15:27.243860",
        }

        response = self.client.post(
            reverse('events_api:events-list'),
            data=data,
            format='json',
            HTTP_AUTHORIZATION="Bearer fake-valid-token",
        )

        self.assertEqual(response.status_code, 202)
        self.assertIsNotNone(Event.objects.all().first())

    @patch.object(ClientTokenBackend, 'decode')
    def test_events_creation_without_timestamp(self, mock_decode):
        mock_decode.return_value = TOKEN_PAYLOAD
        data = {
            "session_id": "s",
            "category": "a",
            "name": "n",
            "data": "{}",
        }

        response = self.client.post(
            reverse('events_api:events-list'),
            data=data,
            format='json',
            HTTP_AUTHORIZATION="Bearer fake-valid-token",
        )

        self.assertEqual(response.status_code, 202)
        self.assertIsNotNone(Event.objects.all().first())
