import uuid

from django.db import models


class ClientCredential(models.Model):
    name = models.CharField(max_length=64)
    client_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    secret_key = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name
