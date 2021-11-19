from datetime import datetime

from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.viewsets import GenericViewSet

from .serializers import EventSerializer
from .tasks import create_event


class EventsViewSet(GenericViewSet):
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        # The only processing done synchronously is attaching the timestamp
        # if not present to avoid loosing the order because of async processing.
        if "timestamp" in request.data:
            create_event.delay(request.data)
        else:
            create_event.delay(
                {**request.data, "timestamp": datetime.utcnow()}
            )
        return Response(status=HTTP_202_ACCEPTED)
