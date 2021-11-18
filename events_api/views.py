from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import EventSerializer


class EventsViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = EventSerializer
