from rest_framework import routers

from events_api.apps import EventsApiConfig
from events_api.views import EventsViewSet

app_name = EventsApiConfig.name

router = routers.SimpleRouter()
router.register(r'', EventsViewSet, basename="events")

urlpatterns = router.urls
