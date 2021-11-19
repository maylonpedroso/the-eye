import logging

from celery import shared_task
from rest_framework.exceptions import ValidationError

from events_api.serializers import EventSerializer

logger = logging.getLogger(__name__)


@shared_task
def create_event(data):
    try:
        serializer = EventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except ValidationError as error:
        logger.error("Invalid event data", exc_info=error)
    except Exception as error:
        logger.error("Error creating event", exc_info=error)
