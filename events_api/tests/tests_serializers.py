from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from events_api.serializers import EventSerializer


class EventSerializerTest(TestCase):
    def test_timestamp_in_the_future_fails_validation(self):
        future = datetime.utcnow() + timedelta(seconds=10)
        serializer = EventSerializer(
            data={
                "session_id": "s",
                "category": "a",
                "name": "n",
                "data": "{}",
                "timestamp": future.isoformat()
            }
        )
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_current_timestamp_passes_validation(self):
        now = datetime.utcnow()
        serializer = EventSerializer(
            data={
                "session_id": "s",
                "category": "a",
                "name": "n",
                "data": "{}",
                "timestamp": now.isoformat()
            }
        )
        self.assertTrue(serializer.is_valid(raise_exception=True))
