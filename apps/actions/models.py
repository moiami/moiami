import uuid

from django.db.models import (
    CASCADE,
    DateTimeField,
    ForeignKey,
    Model,
    UUIDField,
)
from django.utils import timezone

from apps.catalog.models import Movie


class MovieGetAction(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    happened_at = DateTimeField(default=timezone.now, db_index=True)
    user_id = UUIDField(null=True, blank=True, db_index=True)
    movie = ForeignKey(
        Movie,
        on_delete=CASCADE,
        related_name='get_actions',
    )
