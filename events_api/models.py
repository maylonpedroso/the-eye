from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from pytz import utc


def is_no_from_the_future(value):
    if value > datetime.now(tz=utc):
        raise ValidationError("Can not be from the future")


class Event(models.Model):
    session_id = models.CharField(max_length=128)
    category = models.CharField(max_length=128, )
    name = models.CharField(max_length=128)
    data = models.JSONField()
    timestamp = models.DateTimeField(
        default=datetime.utcnow, validators=[is_no_from_the_future]
    )

    class Meta:
        indexes = [
            models.Index(fields=['session_id'], name='session_id_idx'),
            models.Index(fields=['category'], name='category_idx'),
            models.Index(fields=['timestamp'], name='timestamp_idx'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['session_id', 'category', 'name', 'timestamp'],
                name='events_unique',
            )
        ]
